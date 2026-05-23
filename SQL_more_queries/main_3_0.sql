-- user_0d_1 root user and user_0d_2 SELECT and INSERT privileges of the database user_2_db
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS user_2_db;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
