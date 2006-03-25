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
from pisi.actionsapi import get

def build():
    autotools.make("LDFLAGS=\"\"")

def install():
    pisitools.dosbin("syslogd")
    pisitools.dosbin("klogd")
    pisitools.doman("*.[1-9]")
    pisitools.dodoc("ANNOUNCE", "CHANGES", "MANIFEST", "NEWS", "README.1st", "README.linux")
