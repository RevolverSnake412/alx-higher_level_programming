-- Converts 'hbtn_0c_0' database to UTF8.
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p 
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;