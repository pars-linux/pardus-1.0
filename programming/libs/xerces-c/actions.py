#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="xerces-c-src_2_7_0"

def setup():
    shelltools.export("XERCESCROOT","%s" % get.curDIR())
    pisitools.cd("src/xercesc")
    shelltools.system("./runConfigure -plinux -cgcc -xg++ -P/usr")
    
def build():
    pisitools.cd("src/xercesc")
    autotools.make()

def install():
    pisitools.cd("src/xercesc")
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())
   
    pisitools.makedirs("%s/usr/share/doc/xerces-c-2.7.0-1/" % get.installDIR())
    shelltools.copy("../../doc/html","%s/usr/share/doc/xerces-c-2.7.0-1/html" % get.installDIR())

