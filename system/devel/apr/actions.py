#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--datadir=/usr/share/apr-0 \
                         --enable-threads \
                         --enable-nonportable-atomics \
                         --with-devrandom=/dev/urandom")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\" \
                          installbuilddir=/usr/share/apr-0/build" % get.installDIR())

    # bogus values pointing at /var/tmp/pisi/...
    pisitools.dosed("%s/usr/bin/apr-config" % get.installDIR(), \
                    "APR_SOURCE_DIR=.*", \
                    "APR_SOURCE_DIR=/usr/share/apr-0")
    pisitools.dosed("%s/usr/bin/apr-config" % get.installDIR(), \
                    "APR_BUILD_DIR=.*", \
                    "APR_BUILD_DIR=/usr/share/apr-0/build")

    pisitools.dosed("%s/usr/share/apr-0/build/apr_rules.mk" % get.installDIR(), \
                    "apr_builddir=.*", \
                    "apr_builddir=/usr/share/apr-0/build")
    pisitools.dosed("%s/usr/share/apr-0/build/apr_rules.mk" % get.installDIR(), \
                    "apr_builders=.*", \
                    "apr_builders=/usr/share/apr-0/build")

    pisitools.insinto("/usr/share/apr-0/build", "build/*.awk")
    pisitools.insinto("/usr/share/apr-0/build", "build/*.sh")
    pisitools.insinto("/usr/share/apr-0/build", "build/*.pl")

    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE")
