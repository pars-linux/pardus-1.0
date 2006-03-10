#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chgrp plugdev /usr/bin/p*mount*")
    os.system("/usr/bin/chmod 4710 /usr/bin/p*mount*")
