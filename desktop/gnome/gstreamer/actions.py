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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-configdir=/etc/gstreamer \
                        --disable-tests  \
                        --disable-gtk-doc \
                        --disable-examples")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove the unversioned binaries gstreamer provide        
    for file in shelltools.ls("%s/usr/bin/*-0.8" % get.installDIR()):
        deletedFile = file.replace("-0.8", "")
        deletedFile = deletedFile.replace(get.installDIR(), "")
        pisitools.remove(deletedFile)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "DEVEL" \
                    "NEWS", "README", "RELEASE", "REQUIREMENTS", "TODO")
