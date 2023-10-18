-- script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server

-- Prepare and execute a dynamic SQL statement to retrieve table information
SET @query = CONCAT('SELECT COLUMN_NAME, DATA_TYPE, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY, EXTRA FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = "', ? , '" AND TABLE_NAME = "first_name"');
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
