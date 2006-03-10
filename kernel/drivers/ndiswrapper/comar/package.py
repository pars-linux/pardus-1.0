#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/modules-update")
