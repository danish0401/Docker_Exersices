#!/bin/bash
/etc/init.d/mysql stop
service mysql stop
killall -KILL mysql mysqld_safe mysqld
/etc/init.d/mysql start
service mysql start
