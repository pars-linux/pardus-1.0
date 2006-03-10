#!/usr/bin/python

import os
import shutil

def postInstall():
    # Changes should be made to /etc/fonts/local.conf, and as we had
    # too much problems with broken fonts.conf, we force update it ...
    try:
        shutil.move('/etc/fonts/fonts.conf.new', '/etc/fonts/fonts.conf')
    except:
        # for orginal script's mv -f
        pass
    
    os.spawnle(os.P_WAIT, "/usr/bin/fc-cache", "/usr/bin/fc-cache", { "HOME": "/root/" })
