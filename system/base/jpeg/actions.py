#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure", "$srcdir/ltmain.sh", "$srcdir/ltmain.sh $CHOST")
    autotools.configure("--enable-shared --enable-static")
                
def build():
    autotools.make()

def install():
    # create needed diretories for install
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man/man1")

    autotools.rawInstall("prefix=%s/usr libdir=%s/usr/lib mandir=%s/usr/share/man/man1" % (get.installDIR(), get.installDIR(), get.installDIR()))

    pisitools.insinto("/usr/include", "jpegint.h")

    pisitools.dodoc("README", "install.doc", "usage.doc", "wizard.doc", "change.log", "libjpeg.doc", "example.c", "structure.doc", "filelist.doc", "coderules.doc")
