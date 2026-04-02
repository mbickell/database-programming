-- Adminer 4.7.6 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `electricity`;
CREATE TABLE `electricity` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `property` bigint(20) NOT NULL,
  `timestamp` datetime NOT NULL,
  `value` decimal(10,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property` (`property`),
  CONSTRAINT `electricity_ibfk_1` FOREIGN KEY (`property`) REFERENCES `property` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `property`;
CREATE TABLE `property` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `location` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


-- 2026-04-02 05:18:42