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
from pisi.actionsapi import get

WorkDir = "microcode_ctl-1.11"

def build():
    autotools.make("CC=\"%s\" CFLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))
                            

def install():
    pisitools.dosbin("microcode_ctl")
    pisitools.doman("microcode_ctl.8")
    pisitools.dodoc("Changelog", "README")

    pisitools.insinto("/etc", "intel-ia32microcode-*.txt", "microcode.dat")


