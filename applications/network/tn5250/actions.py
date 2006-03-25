#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get 

def setup():
    autotools.configure("--with-x \
                         --with-ssl \
                         --with-slang")

def configure():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/terminfo")
    autotools.rawInstall("DESTDIR=%s \
                          TERMINFO=%s/usr/share/terminfo" % (get.installDIR(), get.installDIR()))

    
    pisitools.dodoc("AUTHORS", "BUGS", "NEWS", "README", "README.ssl", "TODO")
    pisitools.dohtml("doc/*")
