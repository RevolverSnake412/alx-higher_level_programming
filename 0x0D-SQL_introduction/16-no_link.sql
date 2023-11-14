-- Lists all records of second_table.
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <db>
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
