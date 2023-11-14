-- Updates score of Bob to 10 in second_table.
-- [Usage]: cat <file-name> | mysql -hlocalhost -uroot -p <db>
UPDATE second_table SET score = 10 WHERE name = 'Bob';
