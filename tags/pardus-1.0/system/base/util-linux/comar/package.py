#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# real script

tz_file = "/etc/localtime"
tz_zones = "/usr/share/zoneinfo/"

# Default timezone for Pardus
default_zone = "Turkey"

def postInstall():
    if os.path.exists(tz_file):
        if os.path.islink(tz_file):
            # user already set a timezone, no problem
            return
        else:
            # KDE copies timezone data for supporting nfs mounted
            # /usr partitions, we dont
            try:
                os.unlink(tz_file)
            except:
                pass
    os.symlink(os.path.join(tz_zones, default_zone), tz_file)

