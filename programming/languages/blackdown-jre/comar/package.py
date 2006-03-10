#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/find /opt/blackdown-jre -type f -name \"*.so\" -exec chmod +x \{\} \;")
