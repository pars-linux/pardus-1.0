#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("strace")
    pisitools.dobin("strace-graph")
    pisitools.doman("strace.1")
    pisitools.dodoc("ChangeLog", "CREDITS", "NEWS", "PORTING", "README*", "TODO")
