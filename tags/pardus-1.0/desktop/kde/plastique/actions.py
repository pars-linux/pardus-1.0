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

WorkDir = "polymer-0.3.2"

def setup():
    autotools.configure("--enable-mmx")
    
def build():
    autotools.make()
    
def install():
    pisitools.insinto("/usr/qt/3/plugins/styles", "style/libpolymer.so.1.0.0", "polymer.so")
    pisitools.insinto("/usr/bin", "config/polymer-config")
