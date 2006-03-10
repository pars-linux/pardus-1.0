#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE","khexedit kregexpeditor kedit kdessh")
    kde.configure("--without-snmp --without-xmms")

def build():
    kde.make()
    
def install():
    kde.install()

    pisitools.remove("/usr/kde/3.5/share/applications/kde/kwalletmanager.desktop")
