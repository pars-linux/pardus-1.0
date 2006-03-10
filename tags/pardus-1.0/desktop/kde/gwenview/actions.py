#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    # Let filter visibility flags that will *really* hurt
    pisitools.dosed("configure", "-fvisibility=hidden")
    pisitools.dosed("configure", "-fvisibility-inlines-hidden")
    kde.configure()
    
def build():
    kde.make()
    
def install():
    kde.install()

    # Remove gwenview.desktop, we have a custom one
    pisitools.remove("/usr/kde/3.5/share/applications/kde/gwenview.desktop")
