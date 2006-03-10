#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Nihat Ciddi <nakof@zig.gen.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-readline")
    
def build():
    autotools.make()
    
def install():
    pisitools.dobin("bc/bc")
    pisitools.dobin("dc/dc")
    pisitools.doman("man/*.1")
    pisitools.doinfo("doc/*.info")
    pisitools.dodoc("AUTHORS", "FAQ", "NEWS", "README", "ChangeLog")
