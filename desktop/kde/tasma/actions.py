#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import autotools

def setup():
    autotools.make("-f admin/Makefile.common")
    autotools.rawConfigure()
    
def build():
    kde.make()
    
def install():
    kde.install()
