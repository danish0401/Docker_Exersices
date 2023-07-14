create database geeklogin;
use geeklogin;

CREATE TABLE IF NOT EXISTS `accounts` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`password` varchar(255) NOT NULL,
`email` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
);

INSERT INTO accounts VALUES (NULL, 'danish', 'danish', 'danish@123.com')