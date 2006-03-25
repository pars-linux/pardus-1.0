#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/lib/firmware", "*.fw")
    pisitools.insinto("/lib/firmware", "LICENSE", "ipw2100-1.3-LICENSE")
