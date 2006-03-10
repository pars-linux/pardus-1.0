#!/usr/bin/python

import os

def postInstall():
    os.popen("/sbin/init U &> /dev/null")
