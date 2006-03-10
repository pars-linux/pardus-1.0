#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Timu EREN <selamtux@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "cdk-4.9.10-20020809"

def setup():
    autotools.configure("--with-ncurses")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                                     DOCUMENT_DIR=%s" % ( get.installDIR(), get.docDIR() ) )
