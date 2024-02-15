-- prepares a MySQL server for the project
-- nfUhy01uMb9#

CREATE DATABASE IF NOT EXISTS plt_dev_db;
CREATE USER IF NOT EXISTS 'plt_dev'@'localhost' IDENTIFIED BY 'nfUhy01uMb9#';
GRANT ALL PRIVILEGES ON `plt_dev_db`.* TO 'plt_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'plt_dev'@'localhost';
FLUSH PRIVILEGES;
