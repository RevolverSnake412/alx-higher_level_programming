-- Lists all records with a score >= 10 in second_table.
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <db>
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
