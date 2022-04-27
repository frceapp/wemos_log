-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.7.33 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for aplikasi_db
CREATE DATABASE IF NOT EXISTS `aplikasi_db` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `aplikasi_db`;

-- Dumping structure for table aplikasi_db.admin
CREATE TABLE IF NOT EXISTS `admin` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `role` enum('Admin','Member','Wibu') NOT NULL DEFAULT 'Member',
  `time` varchar(50) DEFAULT NULL,
  `status` enum('On','Off') DEFAULT 'Off'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table aplikasi_db.admin: ~5 rows (approximately)
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
REPLACE INTO `admin` (`username`, `password`, `role`, `time`, `status`) VALUES
	('Alim', '123', 'Admin', '08:49', 'Off'),
	('Gharu', '123', 'Wibu', '07:49', 'Off'),
	('Hilmi', '123', 'Wibu', '07:50', 'Off'),
	('Enzo', '123', 'Wibu', '07:50', 'Off'),
	('Tejo', '123', 'Admin', '07:52', 'Off');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;

-- Dumping structure for table aplikasi_db.wemos_log
CREATE TABLE IF NOT EXISTS `wemos_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` varchar(50) NOT NULL DEFAULT '0',
  `time` varchar(50) NOT NULL DEFAULT '0',
  `tanggal` varchar(20) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

-- Dumping data for table aplikasi_db.wemos_log: ~15 rows (approximately)
/*!40000 ALTER TABLE `wemos_log` DISABLE KEYS */;
REPLACE INTO `wemos_log` (`id`, `data`, `time`, `tanggal`, `username`) VALUES
	(1, 'Offline', '08:26', '18 April 2022', 'Tejo'),
	(2, 'Offline', '08:26', '18 April 2022', 'Tejo'),
	(3, 'Offline', '08:27', '18 April 2022', 'Alim'),
	(4, 'Offline', '08:28', '18 April 2022', 'Alim'),
	(5, 'Offline', '08:28', '18 April 2022', 'Alim'),
	(6, 'Offline', '08:28', '18 April 2022', 'Alim'),
	(7, 'Online', '09:25', '20 April 2022', 'neko'),
	(8, '\'Online\'', '07:03', '25 April 2022', '\'Tejo\''),
	(9, '\'Online\'', '07:03', '25 April 2022', '\'Tejo\''),
	(10, 'Online', '07:05', '25 April 2022', 'Tejo'),
	(11, 'Online', '07:05', '25 April 2022', 'Tejo'),
	(12, 'Online', '07:08', '25 April 2022', 'Tejo'),
	(13, 'Online', '10:12', '26 April 2022', 'Tejo'),
	(14, 'Online', '10:12', '26 April 2022', 'Tejo'),
	(15, 'Online', '10:12', '26 April 2022', 'Tejo'),
	(16, 'Feeding', '08:05', '27 April 2022', 'Tejo'),
	(17, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(18, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(19, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(20, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(21, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(22, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(23, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(24, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(25, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(26, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(27, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(28, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(29, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(30, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(31, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(32, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(33, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(34, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(35, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(36, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(37, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(38, 'Feeding', '08:06', '27 April 2022', 'Tejo'),
	(39, 'Feeding', '08:06', '27 April 2022', 'Tejo');
/*!40000 ALTER TABLE `wemos_log` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
