-- Removes all records with a score <= 5 in second_table.
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <db>
DELETE FROM second_table WHERE score <= 5;
