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
from pisi.actionsapi import get

def setup():
    # Use external one!
    pisitools.dosed("libmng_types.h", "#include \"lcms.h\"", "#include <lcms/lcms.h>")

    autotools.configure()

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())

    pisitools.dodoc("Changes", "LICENSE", "README*", "doc/doc.readme", "doc/libmng.txt")

    pisitools.doman("doc/man/*")
    pisitools.dohtml("doc")
