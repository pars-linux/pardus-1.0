#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <meren@pardus.org.tr> 

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="kio-to-local"

def build():
    scons.make()
    
def install():
    pisitools.dodir("/usr/bin")
    shelltools.copy("kio-to-local","%s/usr/bin/kio-to-local" % get.installDIR())
