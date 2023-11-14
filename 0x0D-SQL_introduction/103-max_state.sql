-- Displays the max temp of each state, ordered by state name.
-- [Usage]: <file-name> | mysql -hlocalhost -uroot -p <db>
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;