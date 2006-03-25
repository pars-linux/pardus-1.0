#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.configure()
    shelltools.unlink("db/source/driver/stp.xml")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.system("chmod -R 0644 %s/usr/share/foomatic/db/*" % get.installDIR())
    shelltools.chmod("%s/usr/share/foomatic/db/source" % get.installDIR())
    shelltools.chmod("%s/usr/share/foomatic/db/source/printer" % get.installDIR())
    shelltools.chmod("%s/usr/share/foomatic/db/source/opt" % get.installDIR())
    shelltools.chmod("%s/usr/share/foomatic/db/source/driver" % get.installDIR())

