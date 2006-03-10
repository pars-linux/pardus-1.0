#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    # Shared objects are compiled properly with -fPIC, but
    # standard libs also require this.
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())

    autotools.configure("--without-debug \
                         --enable-largefile \
                         --enable-widec \
                         --libdir=/lib \
                         --with-terminfo-dirs='/etc/terminfo:/usr/share/terminfo' \
                         --disable-termcap \
                         --with-shared \
                         --with-rcs-ids \
                         --without-ada \
                         --enable-symlinks")

def build():
    autotools.make("-j1 sources")
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 

    pisitools.domove("/lib/libform*", "/usr/lib")
    pisitools.domove("/lib/libmenu*", "/usr/lib")
    pisitools.domove("/lib/libpanel*", "/usr/lib")
    pisitools.domove("/lib/*.a", "/usr/lib")

    libtools.gen_usr_ldscript("libncursesw.so")
    libtools.gen_usr_ldscript("libcursesw.so")

    for file in shelltools.ls(get.installDIR() + "/usr/lib/*w.*"):
        source = file.replace(get.installDIR(), "")
        destination = source.replace("w.", ".")
        pisitools.dosym(source, destination)

    for file in shelltools.ls(get.installDIR() + "/lib/libncursesw.so*"):
        source = file.replace(get.installDIR(), "")
        destination = source.replace("w.", ".")
        pisitools.dosym(source, destination)

    # We need the basic terminfo files in /etc
    terminfo = ["ansi", "console", "dumb", "linux", "rxvt", "screen", "sun", \
                "vt52", "vt100", "vt102", "vt200", "vt220", "xterm", "xterm-color", "xterm-xfree86"]

    for file in terminfo:
        termfile = file[0] + "/" + file
        if shelltools.can_access_file("/usr/share/terminfo/%s" % termfile):
            pisitools.dodir("/etc/terminfo/%s" % file[0])
            pisitools.domove("/usr/share/terminfo/%s" % termfile, "/etc/terminfo/%s" % file[0])
            pisitools.dosym("../../../../etc/terminfo/%s/%s" % (file[0], file ), "/usr/share/terminfo/%s/%s" % (file[0], file ))

   # Build fails to create this ...
    pisitools.dosym("../share/terminfo", "/usr/lib/terminfo")

    pisitools.dodoc("ANNOUNCE", "MANIFEST", "NEWS", "README*", "TO-DO", "doc/*.doc")
    pisitools.dohtml("doc/html/")
