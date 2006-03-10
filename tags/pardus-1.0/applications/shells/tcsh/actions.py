#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="tcsh-6.14.00"

def setup():
    autotools.configure("--bindir=%s/bin" % get.installDIR())

def build():
    autotools.make()
    
def install():
    autotools.install()
