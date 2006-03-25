#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def build():
    autotools.make("-C /lib/modules/%s/build M=`pwd`" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/net/wireless" % get.curKERNEL(), "*.ko")

    pisitools.dodoc("Changelog", "README")
