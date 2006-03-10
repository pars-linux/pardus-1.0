# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "giFTcurs-0.6.2"

def setup():
    autotools.configure("--enable-nls")
    
def build():
    autotools.make()
    
def install():
    autotools.install()
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "THANKS", "TODO")        
