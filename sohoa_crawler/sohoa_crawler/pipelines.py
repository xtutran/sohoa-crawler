# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from hashlib import md5
from scrapy import log
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import json

class SohoaPipeline(object):
    """A pipeline to store the item in a MySQL database.
    This implementation uses Twisted's asynchronous database API.
    """

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=3306,
            charset='utf8',
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        # run db query in the thread pool
        d = self.dbpool.runInteraction(self._do_upsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        # at the end return the item in case of success or failure
        d.addBoth(lambda _: item)
        # return the deferred instead the item. This makes the engine to
        # process next item (according to CONCURRENT_ITEMS setting) after this
        # operation (deferred) has finished.
        return d

    def _do_upsert(self, conn, item, spider):
        """Perform an insert or update."""
        guid = self._get_guid(item)
        ##now = datetime.utcnow().replace(microsecond=0).isoformat(' ')

        conn.execute("""SELECT EXISTS(
            SELECT url FROM sohoa_page WHERE guid = %s
        )""", (guid, ))
        ret = conn.fetchone()[0]

        if ret:
            conn.execute("""
                UPDATE sohoa_page
                SET url=%s, title=%s, description=%s, content=%s
                WHERE guid=%s
            """, (item['url'], item['title'], item['description'], item['content'], guid))

            print 'Update ' + str(code) + ' page!'
            self._insert_comment(conn, guid, item)
            
            spider.log("Item updated in db: %s %r" % (guid, item))
        else:
            
            code = conn.execute("""
                INSERT INTO sohoa_page (guid, url, title, description, content)
                VALUES (%s, %s, %s, %s, %s)
            """, (guid, item['url'], item['title'], item['description'], item['content']))

            print 'Insert ' + str(code) + ' page!'
            self._insert_comment(conn, guid, item)
            
            spider.log("Item stored in db: %s %r" % (guid, item))

    def _insert_comment(self, conn, guid, item):

        print 'Insert Comment'
        comments = self._parse_comment(item)
        comment_id = 0
        for comment in comments:
            
            conn.execute("""
                INSERT INTO sohoa_comment (comment_id, page_id, comment_text)
                VALUES (%s, %s, %s)
            """, (comment_id, guid, comment))
            comment_id = comment_id + 1

    def _parse_comment(self, item):
        comments = []
        with open('comments.json') as data_file:
            data = json.load(data_file)
            for item in data['data']['items']:
                comment = item['content'].strip().encode('utf8')
                print 'comment: ' + comment
                comments.append(comment)

                for reply_item in item['replys']['items']:
                    comment = reply_item['content'].strip().encode('utf8')
                    print 'reply: ' + comment
                    comments.append(comment)
                    
        return (comments)
        
    def _handle_error(self, failure, item, spider):
        """Handle occurred on db interaction."""
        # do nothing, just log
        log.err(failure)

    def _get_guid(self, item):
        """Generates an unique identifier for a given item."""
        # hash based solely in the url field
        return md5(item['url']).hexdigest()

