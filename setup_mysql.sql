-- prepares a MySQL server for the project
-- nfUhy01uMb9#

CREATE DATABASE IF NOT EXISTS plt_test_db;
CREATE USER IF NOT EXISTS 'plt_test'@'localhost' IDENTIFIED BY 'nfUhy01uMb9#';
GRANT ALL PRIVILEGES ON `plt_test_db`.* TO 'plt_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'plt_test'@'localhost';
FLUSH PRIVILEGES;
