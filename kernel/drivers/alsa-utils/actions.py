#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gökçen Eraslan <gokcene@anadolu.edu.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())
    pisitools.dodoc("ChangeLog", "README", "TODO", "seq/aconnect/README.aconnect", "seq/aseqnet/README.aseqnet")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcTAG(),"alsamixer/README", "README.alsamixer")
