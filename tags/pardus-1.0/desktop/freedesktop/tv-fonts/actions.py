#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/X11/fonts/xawtv", "*.gz")
    pisitools.insinto("/usr/lib/X11/fonts/xawtv", "fonts.alias")
    
    shelltools.cd("%s/usr/lib/X11/fonts/xawtv" % get.installDIR())
    shelltools.system("mkfontdir")

