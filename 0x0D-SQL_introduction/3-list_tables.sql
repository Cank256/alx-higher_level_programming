-- A script that lists all the tables of a database in your MySQL server.

-- Set the user-defined variable @dbname to the first argument passed to the script
SET @dbname = ?;

-- Use the selected database to show tables
USE @dbname;
SHOW TABLES;
