-- Displays the avg temp (Fahrenheit) by city ordered by temperature (descending).
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <db>
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;