-- Lists the number of records with the same score in second_table.
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <db>
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score;
