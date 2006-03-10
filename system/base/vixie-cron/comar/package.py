#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown -R root:cron /var/spool/cron")
    os.system("/usr/bin/chmod -R 0750 /var/spool/cron")
    
    os.system("/usr/bin/chmod 0755 /etc/conf.d")
    
    os.system("/usr/bin/chmod 0644 /etc/pam.d/cron")

    os.system("/usr/bin/chown root:wheel /usr/sbin/cron")
    os.system("/usr/bin/chmod 0750 /usr/sbin/cron")

    os.system("/usr/bin/chown root:cron /usr/bin/crontab")
    os.system("/usr/bin/chmod 4750 /usr/bin/crontab")
