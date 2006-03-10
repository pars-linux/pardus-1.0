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
    # Python bindings disabled because it needs python > 2.4
    autotools.configure("--with-xml=libxml\
                        --disable-mono-docs \
                        --with-x \
                        --enable-gtk \
                        --enable-qt3 \
                        --enable-python \
                        --disable-mono \
                        --enable-glib \
                        --enable-verbose-mode \
                        --enable-checks \
                        --enable-asserts \
                        --with-system-pid-file=/var/run/dbus.pid \
                        --with-system-socket=/var/lib/dbus/system_bus_socket \
                        --with-session-socket-dir=/tmp \
                        --with-dbus-user=messagebus \
                        --enable-doxygen-docs \
                        --disable-xml-docs")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/bin/dbus-daemon", "/usr/bin/dbus-daemon-1")

    # needs to exist for the system socket
    pisitools.dodir("/var/lib/dbus")
    pisitools.dodir("usr/lib/dbus-1.0/services")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "doc/TODO")
    pisitools.dohtml("doc/")
