#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.install()
    pisitools.doman("scons.1", "sconsign.1")
