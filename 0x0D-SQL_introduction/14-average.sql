-- Computes the score average of all records in second_table.
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <db>
SELECT AVG(score) AS average FROM second_table;
