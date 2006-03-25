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

def setup():
    pisitools.dosed("pth_string.c", "pow10" ,"math_pow10")
    pisitools.dosed("pth_string.c","round" ,"math_round")
                    
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ANNOUNCE", "AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "USERS")
