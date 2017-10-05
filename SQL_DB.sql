create database if not exists TheDB;

use TheDB;

CREATE TABLE IF NOT EXISTS TheTable (
    `index` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `key` VARCHAR(255) NOT NULL,
    `value` VARCHAR(255) NOT NULL
);
    
drop table TheTable;

SELECT 
    *
FROM
    TheTable;