#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chmod -R 0750 /var/lib/mysql")
    os.system("/usr/bin/chown -R mysql:mysql /var/lib/mysql")

    os.system("/usr/bin/chmod 0750 /var/log/mysql")
    os.system("/usr/bin/chmod -R 0660 /var/log/mysql/*")
    os.system("/usr/bin/chown -R mysql:mysql /var/log/mysql")

    os.system("/usr/bin/chmod -R 0755 /var/run/mysqld")
    os.system("/usr/bin/chown -R mysql:mysql /var/run/mysqld")
