-- create a user with only read access to database
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- create a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- grant read access to the new user
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
