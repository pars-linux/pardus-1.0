#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/libexec/opengl-update nvidia")
