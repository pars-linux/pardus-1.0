#!/usr/bin/python

import os

def postInstall():
    os.spawnl(os.P_WAIT, "/usr/bin/gst-register-0.8", "/usr/bin/gst-register-0.8")
