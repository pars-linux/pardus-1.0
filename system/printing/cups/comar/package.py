#/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/install -d -m0755 /var/log/cups")
    os.system("/usr/bin/install -d -m0755 /var/spool")
    os.system("/usr/bin/install -m0700 -o lp -d /var/spool/cups")
    os.system("/usr/bin/install -m1700 -o lp -d /var/spool/cups/tmp")
    os.system("/usr/bin/install -m0711 -o lp -d /etc/cups/certs")
    os.system("/usr/bin/install -d -m0755 /etc/cups/{interfaces,ppd}")

    os.system("/sbin/rc-update add cupsd default")
    os.system("/sbin/depscan.sh")
