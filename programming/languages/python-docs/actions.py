#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Python-Docs-2.4.2"

def install():
    pisitools.insinto("%s/%s/html" % (get.docDIR(), get.srcTAG()), "*")
