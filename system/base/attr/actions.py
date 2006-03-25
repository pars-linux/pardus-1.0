#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--libdir=/lib \
                            --libexecdir=/usr/libexec \
                            --bindir=/bin") 
def build():
    autotools.make()

def install():
    pisitools.removeDir("/usr/man/man2")
    autotools.make("DIST_ROOT=%s install install-lib install-dev" % get.installDIR())
    
