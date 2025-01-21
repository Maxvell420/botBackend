CREATE USER '{$MYSQL_USER}'@'{$DB_DATABASE}' IDENTIFIED BY '{$MYSQL_PASSWORD}';
GRANT CREATE, SELECT, INSERT, UPDATE, DELETE ON *.* TO '{$MYSQL_USER}'@'{$DB_DATABASE}';
FLUSH PRIVILEGES;