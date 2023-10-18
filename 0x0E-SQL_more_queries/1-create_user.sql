-- Create or update user_0d_1 with all privileges and set the password
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *. * TO 'user_0d_1'@'%';
