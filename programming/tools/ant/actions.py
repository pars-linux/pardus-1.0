#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
import os

WorkDir="apache-ant-1.6.5"

def build():
    shelltools.system("./bootstrap.sh")

def install():
    
    BINS=("antRun", "complete-ant-cmd.pl", "runant.pl", "runant.py")

    pisitools.cd("bootstrap/bin")
    for bin in BINS:
        pisitools.dobin(bin)
        pisitools.dosym("/usr/bin/%s" % bin, "/usr/share/ant-core/bin/%s" % bin)

    pisitools.dobin("ant")
    pisitools.cd("../lib")
    pisitools.insinto("/usr/share/ant-tasks/lib/", "*.jar")

    for jar in os.listdir("."):
        pisitools.dosym("/usr/share/ant-tasks/lib/%s" % jar, "/usr/share/ant-core/lib/%s" % jar)
