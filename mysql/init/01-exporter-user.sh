#!/bin/sh
set -eu

exporter_password="$(cat /run/secrets/mysql_exporter_password)"
escaped_password="$(printf '%s' "$exporter_password" | sed "s/'/''/g")"

mysql --protocol=socket -uroot -p"$(cat /run/secrets/mysql_root_password)" <<-EOSQL
CREATE USER IF NOT EXISTS 'exporter'@'%' IDENTIFIED BY '${escaped_password}';
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';
FLUSH PRIVILEGES;
EOSQL

