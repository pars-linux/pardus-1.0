#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE","kandy korn")
    kde.configure("--with-sasl \
                   --without-gnokii")

def build():
    kde.make()

def install():
    kde.install()
    pisitools.remove("%s/share/autostart/korgac.desktop" % get.kdeDIR())
