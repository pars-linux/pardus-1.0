#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gökçen Eraslan <gokcene@anadolu.edu.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("reiserfsck", "/sbin/fsck.reiserfs")
    pisitools.dosym("mkreiserfs", "/sbin/mkfs.reiserfs")
    pisitools.dodoc("ChangeLog", "INSTALL", "README")
