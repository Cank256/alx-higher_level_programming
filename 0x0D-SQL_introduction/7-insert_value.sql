-- MySQL script to insert a new row in the table first_table (database hbtn_0c_0) 
-- with id = 89 and name = Best School, passing the database name as an argument of the mysql command
USE @dbname;
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
