#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "device-mapper.1.01.05"

def setup():
    autotools.configure()

def build():
    # has trouble with parallel building
    autotools.make("-j1")

def install():
    autotools.install("sbindir=\"%s/sbin\" libdir=\"%s/lib\"" % (get.installDIR(), get.installDIR()))

    pisitools.dolib_a("lib/ioctl/libdevmapper.a")
    libtools.gen_usr_ldscript("libdevmapper.so")


    pisitools.dodoc("COPYING*", "INSTALL", "INTRO", "README", "VERSION", "WHATS_NEW")


