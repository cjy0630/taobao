CREATE DATABASE `taobao` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
CREATE TABLE `comment` (
  `comment_id` varchar(45) NOT NULL,
  `keyword` varchar(45) DEFAULT NULL,
  `item_id` varchar(45) DEFAULT NULL,
  `user_id` varchar(45) DEFAULT NULL,
  `title` longtext,
  `comment_user` varchar(45) DEFAULT NULL,
  `rate_content` longtext,
  `rate_date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `grab_records` (
  `grab_id` varchar(45) NOT NULL,
  `title` longtext,
  `grab_url` longtext,
  PRIMARY KEY (`grab_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

