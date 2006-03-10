#!/usr/bin/python

import os

def postInstall():
    os.popen("/sbin/modules-update")
