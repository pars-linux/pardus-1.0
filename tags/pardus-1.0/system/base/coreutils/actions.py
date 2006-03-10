#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.move("m4/inttypes.m4", "m4/inttypes-eggert.m4")
    shelltools.touch("aclocal.m4")
    shelltools.touch("configure")
    shelltools.touch("config.hin")
    shelltools.touch("Makefile.in")
    shelltools.touch("*/Makefile.in")
    shelltools.touch("*/*/Makefile.in")

    # Fix issues with gettext's autopoint if cvs is not installed,
    shelltools.export("AUTOPOINT", "/bin/true")

    # Reconfiguring configure scripts
    shelltools.export("WANT_AUTOMAKE", "1.8")
    shelltools.export("WANT_AUTOCONF", "2.5")

    shelltools.system("autoreconf --force --install")
    autotools.configure("--bindir=/bin --enable-largefile --enable-nls")
                        
def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move non-critical packages into /usr
    non_critical = ["csplit", "expand", "factor", "fmt", "fold", "join", \
                    "md5sum", "nl", "od", "paste", "pathchk", "pinky", \
                    "pr", "printf", "sha1sum", "shred", "sum", "tac", \
                    "tail", "test", "[", "tsort", "unexpand", "users"]
    
    for file in non_critical:
        pisitools.domove("/bin/%s" % file, "/usr/bin/", file)
    
    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")

    for file in shelltools.ls("%s/bin/" % get.installDIR()):
        pisitools.dosym("/bin/%s" % file, "/usr/bin/%s" % file)
