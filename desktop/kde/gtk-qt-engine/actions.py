#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "gtk-qt-engine"

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure("--with-arts")

def build():
    kde.make()
    
def install():
    kde.install()

    pisitools.remove("/usr/kde/3.5/share/applnk/Settings/LookNFeel/kcmgtk.desktop")
