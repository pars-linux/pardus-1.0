#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure("/usr")
                      
def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("README", "Changes")
