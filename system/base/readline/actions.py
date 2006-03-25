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
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-curses --libdir=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())
    
    pisitools.domove("/usr/lib/*.so*", "/lib")
    shelltools.chmod("%s/lib/*.so*" % get.installDIR())

    # workaround for #1074, will investigate later
    # libtools.gen_usr_ldscript("libreadline.so")
    # libtools.gen_usr_ldscript("libhistory.so")

    pisitools.dosym("/usr/lib/libreadline.so", "/usr/lib/libreadline.so.5")

    pisitools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS", "doc/*.ps")
    pisitools.dohtml("doc/")
