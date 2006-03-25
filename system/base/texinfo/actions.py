#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/texinfo.txi", "setfilename texinfo", "setfilename texinfo.info")
    pisitools.dosed("doc/Makefile.in", "INFO_DEPS = texinfo", "INFO_DEPS = texinfo.info")
    pisitools.dosed("doc/Makefile.in", "texinfo:", "texinfo.info:")
    
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())    
 
    # tetex installs this guy #76812
    pisitools.remove("/usr/bin/texi2pdf")

    pisitools.dodoc("AUTHORS", "ChangeLog", "INTRODUCTION", "NEWS", "README", "TODO")
    pisitools.newdoc("info/README", "README.info")
    pisitools.newdoc("makeinfo/README", "README.makeinfo")
