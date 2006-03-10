#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@haftalik.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/screen.1", "/usr/local/etc/screenrc", "/etc/screenrc")
    pisitools.dosed("doc/screen.1", "/usr/local/screens", "/var/run/screen")
    pisitools.dosed("doc/screen.1", "/local/etc/screenrc", "/etc/screenrc")
    pisitools.dosed("doc/screen.1", "/etc/utmp", "/var/run/utmp")
    pisitools.dosed("doc/screen.1", "/local/screens/S-", "/var/run/screen/S-")

    shelltools.export("CFLAGS", "%s -DPTYMODE=0620 -DPTYGROUP=5 -DUSE_PAM" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -DPTYMODE=0620 -DPTYGROUP=5 -DUSE_PAM" % get.CXXFLAGS())

    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.autoconf()

    autotools.configure("--enable-pam \
                         --with-socket-dir=/var/run/screen \
                         --with-sys-screenrc=/etc/screenrc \
                         --enable-rxvt_osc")

def build():
    autotools.make("term.h")
    autotools.make()

def install():
    pisitools.dobin("screen")

    pisitools.dodir("/var/run/screen")
    pisitools.dodir("/etc/pam.d")

    pisitools.insinto("/usr/share/terminfo", "terminfo/screencap")
    pisitools.insinto("/usr/share/screen/utf8encodings", "utf8encodings/??")

    pisitools.dodoc("README", "ChangeLog", "INSTALL", "TODO", "NEWS*", \
                    "patchlevel.h", "doc/FAQ", "doc/README.DOTSCREEN", "doc/fdpat.ps", "doc/window_to_display.ps")

    pisitools.doman("doc/screen.1")
    pisitools.doinfo("doc/screen.info*")

    shelltools.chmod("%s/var/run/screen" % get.installDIR(), 0775)
