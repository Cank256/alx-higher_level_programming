-- script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server
SELECT column_name, data_type, column_default, is_nullable, character_maximum_length, column_type, column_key, extra
FROM information_schema.columns
WHERE table_name = 'first_table'
