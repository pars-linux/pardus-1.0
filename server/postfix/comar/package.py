#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/postconf -c \"/etc/postfix\" -e home_mailbox=.maildir/")

    os.system("/usr/bin/chown root:postdrop /usr/sbin/postdrop")
    os.system("/usr/bin/chmod 02711 /usr/sbin/postdrop")

    os.system("/usr/bin/chown root:postdrop /usr/sbin/postqueue")
    os.system("/usr/bin/chmod 02711 /usr/sbin/postqueue")

    os.system("/usr/bin/chown root:mail /var/spool/mail")
    os.system("/usr/bin/chmod 0755 /var/spool/mail")
