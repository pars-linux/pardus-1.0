#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("python setup.py build")

def install():
    shelltools.system("python setup.py install --root=%s" % get.installDIR())
