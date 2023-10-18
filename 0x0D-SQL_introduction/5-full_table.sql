-- script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server

SELECT
    'first_table' AS 'Table',
    CONCAT('CREATE TABLE `first_table` (\n', GROUP_CONCAT(COLUMN_NAME, ' ', COLUMN_TYPE, ' ', IF(IS_NULLABLE = 'NO', 'NOT NULL', 'DEFAULT NULL'), ',\n'), ') ENGINE=', ENGINE, ' DEFAULT CHARSET=', CHARACTER_SET_NAME, ' COLLATE=', COLLATION_NAME) AS 'Create Table'
FROM
    information_schema.columns
WHERE
    table_schema = 'hbtn_0c_0'
    AND table_name = 'first_table';