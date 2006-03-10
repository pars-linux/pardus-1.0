#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ali Erdinç Köroğlu <erdinc@erdinc.info>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ndiswrapper-1.7"

def build():
    shelltools.cd("utils/")
    autotools.make("-C /lib/modules/%s/build M=`pwd`" % get.curKERNEL())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodir("/etc/ndiswrapper")
    
    pisitools.dosbin("utils/ndiswrapper", "/usr/sbin")
    pisitools.dosbin("utils/ndiswrapper-buginfo", "/usr/sbin")
    pisitools.dosbin("loadndisdriver", "/sbin")
    
    pisitools.doman("ndiswrapper.8")
    pisitools.dodoc("README", "INSTALL", "AUTHORS", "ChangeLog")
