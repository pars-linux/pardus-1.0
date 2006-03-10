#!/usr/bin/python

import os

def postInstall():
    if os.path.exists("/sbin/mkinitrd"):
        os.system("/sbin/mkinitrd kernel_version=2.6.14.4-15 full")
