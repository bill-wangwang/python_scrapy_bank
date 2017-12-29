-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.18 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 bank 的数据库结构
CREATE DATABASE IF NOT EXISTS `bank` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `bank`;


-- 导出  表 bank.bank_area 结构
CREATE TABLE IF NOT EXISTS `bank_area` (
  `id` char(10) NOT NULL COMMENT '省份（城市）编号',
  `fid` char(10) DEFAULT '' COMMENT '为空时表示省份，否则代表省份编号',
  `name` char(50) DEFAULT '' COMMENT '省份（城市）名称',
  PRIMARY KEY (`id`),
  KEY `fid` (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行省份地区表';

-- 数据导出被取消选择。


-- 导出  表 bank.bank_bank 结构
CREATE TABLE IF NOT EXISTS `bank_bank` (
  `orga_name` char(50) NOT NULL COMMENT '银行名称',
  `paym_numb` char(12) NOT NULL COMMENT '12位联行号（3位银行类型编号 + 4位地区 + 3 位银行编号 + 1位校验码）',
  `bank_type_id` char(3) NOT NULL COMMENT '3位银行类型编号',
  `prov_id` char(3) NOT NULL COMMENT '3位省份编号',
  `city_id` char(4) NOT NULL COMMENT '4位地区号',
  PRIMARY KEY (`paym_numb`),
  KEY `bank_id` (`bank_type_id`),
  KEY `city_id` (`city_id`),
  KEY `prov_id` (`prov_id`),
  KEY `orga_name` (`orga_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行联行号表';

-- 数据导出被取消选择。


-- 导出  表 bank.bank_bank_type 结构
CREATE TABLE IF NOT EXISTS `bank_bank_type` (
  `id` char(3) NOT NULL COMMENT '3位银行编码',
  `name` char(50) DEFAULT NULL COMMENT '银行分类名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行类型表';

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
