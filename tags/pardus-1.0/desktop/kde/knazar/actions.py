#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr> 

from pisi.actionsapi import scons
from pisi.actionsapi import get

def build():
    scons.make()

def install():
    scons.make("prefix=%s/usr/ install" % get.installDIR())
