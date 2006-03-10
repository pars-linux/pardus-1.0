#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/touch /usr/lib/MozillaFirefox/components/compreg.dat")
    os.system("/usr/bin/touch /usr/lib/MozillaFirefox/components/xpti.dat")
    os.system("/usr/lib/MozillaFirefox/firefox -register")
    #FIXME: os.system("/usr/lib/MozillaFirefox/regxpcom")
    
    #Recalculate disk geometry and generate preload file
    os.system("/usr/sbin/prepare_preload_file -c < /etc/preload.d/Firefox.preload_phase2 > /etc/preload.d/Firefox.preload")
