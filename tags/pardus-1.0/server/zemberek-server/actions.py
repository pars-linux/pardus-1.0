#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="zemberek_server-0.3"

def build():
    shelltools.system("ant dist")

def install():
    shelltools.cd("dist/")
    pisitools.insinto("/opt/zemberek-server/config", "config/*")
    pisitools.insinto("/opt/zemberek-server/kaynaklar", "kaynaklar/*")
    pisitools.insinto("/opt/zemberek-server/lib", "lib/*")
    pisitools.insinto("/opt/zemberek-server/lisanlar", "lisanslar/*")
    pisitools.insinto("/opt/zemberek-server", "zemberek_server-0.3.jar")
