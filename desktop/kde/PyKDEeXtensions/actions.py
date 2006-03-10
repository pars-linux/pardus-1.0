#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "pykdeextensions-0.4.0"

def install():
    pythonmodules.run("setup.py install --root=%s" % get.installDIR())
