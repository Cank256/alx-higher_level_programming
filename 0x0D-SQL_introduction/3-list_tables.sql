-- Set the database name using a user-defined variable
SET @dbname = ?;

-- Use the selected database to show tables
USE @dbname;

-- List all tables in the selected database
SHOW TABLES;