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

WorkDir = "iproute2-051007"

def setup():
    pisitools.dosed("Makefile", "-O2", "%s" % get.CFLAGS())

    pisitools.dosed("tc/m_ipt.c", "/usr/local", "/usr")

def build():
    shelltools.echo("Config", "TC_CONFIG_ATM:=n")

    autotools.make("CC=\"%s\" \
                    AR=\"%s\" \
                    SUBDIRS=\"lib ip tc misc netem\" \
                    " % (get.CC(), get.AR()))

def install():
    autotools.rawInstall("DESTDIR=\"%s\" \
                          SBINDIR=/sbin \
                          DOCDIR=/usr/share/doc/%s \
                          " % (get.installDIR(), get.srcTAG()))

    pisitools.dodir("/usr/sbin")
    pisitools.domove("/sbin/arpd", "/usr/sbin/")
