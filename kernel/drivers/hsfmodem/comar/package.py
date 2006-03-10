#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/hsfconfig --serial --region=AUTO --rcscript --auto")
    os.system("/sbin/rc-update del hsf")
    os.system("/sbin/depscan.sh")
    os.system("/sbin/modules-update")
