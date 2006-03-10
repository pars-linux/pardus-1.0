#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown -R root:slocate /var/lib/slocate")
    os.system("/usr/bin/chmod 0750 /var/lib/slocate")
    
    os.system("/usr/bin/chmod 0755 /etc/cron.daily/slocate")

    os.system("/usr/bin/chown root:slocate /usr/bin/slocate")
    os.system("/usr/bin/chmod go-r,g+s /usr/bin/slocate")
