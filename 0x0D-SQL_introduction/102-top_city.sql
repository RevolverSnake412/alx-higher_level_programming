-- Displays the top 3 cities with the highest avg temp between July and August.
-- cat <file-name> | mysql -hlocalhost -uroot -p <db>
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;