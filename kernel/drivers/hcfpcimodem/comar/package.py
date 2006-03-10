#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/hcfpciconfig --serial --region=AUTO --rcscript --auto")
    os.system("/sbin/rc-update del hcfpci")
    os.system("/sbin/depscan.sh")
    os.system("/sbin/modules-update")
