#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import perlmodules

WorkDir = "IO-Socket-SSL-0.96"

def setup():
    perlmodules.configure()
                      
def build():
    perlmodules.make()

def install():
    perlmodules.install()
