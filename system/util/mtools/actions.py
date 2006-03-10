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
    autotools.configure("--sysconfdir=/etc/mtools")

def build():
    autotools.make()

def install():
    autotools.install("sysconfdir=%s/etc/mtools" % get.installDIR())    

    pisitools.insinto("/etc/mtools","mtools.conf")
    pisitools.insinto("/etc/mtools","mtools.conf.example")
    pisitools.dodoc("Changelog", "NEWPARAMS", "README*", "Release.notes")
