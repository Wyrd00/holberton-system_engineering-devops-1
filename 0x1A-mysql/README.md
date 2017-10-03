
# 0x1A. Mysql

This project is about setting up a `Primary-Replica` infrastructure using MySQL.

## Environment
The bash scripts have been tested on Ubuntu 14.05.5 LTS with MySQL version 5.7

Tests done in VirtualBox on [Ubuntu](https://atlas.hashicorp.com/ubuntu/boxes/trusty64) via [Vagrant](https://www.vagrantup.com/)(1.9.1)

## Repository Breakdown
Once cloned over, the repository will contain the following files:

|   **File**    |  **Decription**                       |
|---------------|---------------------------------------|
| 0-mysql_configuration_primary   | MySQL configuration file for primary server (web-01)           |
| 0-mysql_configuration_replica      | MySQL configuration file for replica server (web-02)         |
| 1-mysql_backup     | Bash script that generates a MySQL dump and creates a compressed archive out of it |


## How to Use 1-mysql_backup
To use the bash script, download the file with wget or whatever way preferred.
Once the script is in your local, run the script like so:
```
$ ./1-mysql_backup mydummypassword
```
The first argument is the password for your MySQL database and the output of the archive is like so:

```
$ 01-03-2017.tar.gz  1-mysql_backup  backup.sql
```

The script will dump all your databases into the `sql` file named `backup.sql` and will archive the file with the date format: Month-Date-Year.

Example of a `backup.sql` file:

```
$ more backup.sql

-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database:
-- ------------------------------------------------------
-- Server version   5.5.54-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `holberton`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `holberton` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `holberton`;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
```

## Known Bugs
There are no known bugs at the time.

### Author
*Kimberly Wong* - [Github](https://github.com/kjowong) || [Twitter](https://twitter.com/kjowong) || [email](kimberly.wong@holbertonschool.com)


#### Feedback and contributors welcomed.
