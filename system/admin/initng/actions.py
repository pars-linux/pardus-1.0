#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "initng"

def setup():
    libtools.libtoolize("--force --copy")
    autotools.aclocal()
    autotools.autoheader()
    autotools.autoconf()
    autotools.automake("--add-missing --copy --gnu")
                        
    autotools.configure("--sbindir=/sbin --libdir=/lib")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", \
                    "FAQ", \
                    "AUTHORS", \
                    "ChangeLog", \
                    "NEWS", \
                    "TEMPLATE_HEADER", \
                    "TODO", \
                    "doc/databases.txt", \
                    "doc/empty.conf", \
                    "doc/hard.conf", \
                    "doc/initng.txt")

    # sync with baselayout defaults
    pisitools.dosed("%s/etc/initng/default.runlevel" % get.installDIR(), "daemon/xdm", "daemon/kdm")

    shelltools.echo("%s/etc/initng/default.runlevel" % get.installDIR(), "daemon/comar")
    shelltools.echo("%s/etc/initng/default.runlevel" % get.installDIR(), "daemon/local")
    shelltools.echo("%s/etc/initng/default.runlevel" % get.installDIR(), "daemon/hald")
    shelltools.echo("%s/etc/initng/default.runlevel" % get.installDIR(), "daemon/syslogd")
    shelltools.echo("%s/etc/initng/default.runlevel" % get.installDIR(), "daemon/klogd")
