#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/find /opt/blackdown-jdk -type f -name \"*.so\" -exec chmod +x \{\} \;")
