-- phpMyAdmin SQL Dump
-- version 4.0.9
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2015 at 06:01 AM
-- Server version: 5.5.34
-- PHP Version: 5.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `sohoa_crawler`
--

-- --------------------------------------------------------

--
-- Table structure for table `sohoa_comment`
--

CREATE TABLE IF NOT EXISTS `sohoa_comment` (
  `comment_id` int(11) NOT NULL,
  `page_id` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `comment_text` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`comment_id`,`page_id`),
  KEY `page_id` (`page_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `sohoa_comment`
--

INSERT INTO `sohoa_comment` (`comment_id`, `page_id`, `comment_text`) VALUES
(0, '61cb120b1c623faf13f8cd19bd069e76', 'Kính Microsoft HoloLens mới thực sự là cuộc cách mạng lớn chứ không phải là Oculus Rift'),
(1, '61cb120b1c623faf13f8cd19bd069e76', 'cứ như phim khoa học viễn tưởng ấy nhỉ, mấy ông chỉ đạo quẹt quẹt á hã :D'),
(2, '61cb120b1c623faf13f8cd19bd069e76', 'mọi bộ phim khoa học viễn tưởng đều có cơ sở của nó ^^'),
(3, '61cb120b1c623faf13f8cd19bd069e76', 'Đĩnh của đĩnh. The best of the best'),
(4, '61cb120b1c623faf13f8cd19bd069e76', 'Ôi khi nào mới đc cầm lá "Blue eye dragon" test nhỉ :))'),
(5, '61cb120b1c623faf13f8cd19bd069e76', 'Giống google clasd nhở'),
(6, '61cb120b1c623faf13f8cd19bd069e76', 'Ôi trời công nghệ!!! Tuyệt vời'),
(7, '61cb120b1c623faf13f8cd19bd069e76', 'Trên cả tuyệt vời'),
(8, '61cb120b1c623faf13f8cd19bd069e76', 'MS is back, the Giant of technology. rất ấn tượng với những gì MS đã làm gần đây');

-- --------------------------------------------------------

--
-- Table structure for table `sohoa_page`
--

CREATE TABLE IF NOT EXISTS `sohoa_page` (
  `guid` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `url` text COLLATE utf8_unicode_ci NOT NULL,
  `title` text COLLATE utf8_unicode_ci NOT NULL,
  `description` text COLLATE utf8_unicode_ci NOT NULL,
  `content` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`guid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `sohoa_page`
--

INSERT INTO `sohoa_page` (`guid`, `url`, `title`, `description`, `content`) VALUES
('61cb120b1c623faf13f8cd19bd069e76', 'http://sohoa.vnexpress.net/tin-tuc/san-pham/do-choi-so/dung-thu-kinh-thuc-te-ao-microsoft-hololens-3208049.html', 'Dùng thử kính thực tế ảo Microsoft HoloLens - VnExpress Số Hóa', 'Sau khi công bố vào tháng 1/2015, đây là lần đầu tiên, Microsoft cho phép khách tham dự sự kiện Build trải nghiệm thực tế kính HoloLens.', 'Tập đoàn phần mềm Mỹ chưa tiết lộ khi nào HoloLens sẽ có mặt trên thị trường. Họ cũng đưa ra các quy định nghiêm ngặt đối với các nhà báo muốn dùng kính: Không quay video, chụp ảnh, ghi âm khi tham gia trải nghiệm.\n\n\nTrong màn thử nghiệm đầu tiên, kết hợp với phần mềm kiến trúc SketchUp, người đeo kính có thể kéo các vật thể ra khỏi màn hình. Vật thể đó sẽ biến thành ảnh ảo 3D (3D hologram) ngay trước mắt và người dùng sẽ sử dụng tay di chuyển trong không trung và thực hiện thao tác air-tapping như thể họ đang nhấn vào một con chuột ảo để co kéo, thay đổi kích cỡ, màu sắc… của vật thể nhằm dễ dàng hình dung nó sẽ như thế nào trong không gian thực.\n\nViệc giơ ngón tay ra phía trước và bấm vào các icon (Microsoft gọi là air-tapping) cũng như hiệu ứng âm thanh mô phỏng như trong đời thực mang lại cảm giác đặc biệt, tự nhiên và khác lạ (dù người ngoài nhìn vào có thể thấy bạn trông thật kỳ cục). HoloLens nhận diện chuyển động của ngón tay khá chuẩn và nhanh chóng thực hiện lệnh của người dùng.\n\n');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
