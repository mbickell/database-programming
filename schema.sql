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


DROP VIEW IF EXISTS `fin_prices_2025`;
CREATE TABLE `fin_prices_2025` (`date` date, `price_eur_kwhe` decimal(14,6));


DROP TABLE IF EXISTS `prices`;
CREATE TABLE `prices` (
  `country` varchar(100) NOT NULL,
  `iso3_code` varchar(3) NOT NULL,
  `date` date NOT NULL,
  `price_eur_mwhe` decimal(10,2) NOT NULL,
  PRIMARY KEY (`iso3_code`,`date`),
  KEY `date` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `property`;
CREATE TABLE `property` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `location` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


DROP TABLE IF EXISTS `fin_prices_2025`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `fin_prices_2025` AS select `prices`.`date` AS `date`,`prices`.`price_eur_mwhe` / 1000 AS `price_eur_kwhe` from `prices` where `prices`.`iso3_code` = 'FIN' and `prices`.`date` between '2025-01-01' and '2025-12-31';

-- 2026-04-30 08:26:13