-- Creates a table called first_table in the current DB
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <database-name>
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
