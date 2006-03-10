#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "iputils"

def setup():

    pisitools.dosed("Makefile", "(?m)^(CCOPT=.*)-O2", r"\1" + get.CFLAGS())
    pisitools.dosed("Makefile", "(?m)^(CC=.*)gcc", r"\1" + get.CC())
    pisitools.dosed("Makefile", "/usr/src/linux/include", "/usr/include")
    pisitools.dosed("libipsec/Makefile", "/usr/src/linux/include", "/usr/include")
    pisitools.dosed("setkey/Makefile", "/usr/src/linux/include", "/usr/include")

    pisitools.dosed("Makefile", 'IPV6_TARGETS=", "#IPV6_TARGETS=')
    pisitools.dosed("setkey/Makefile","-ll" ,"-lfl ${LDFLAGS}")
    pisitools.dosed("libipsec/Makefile", "yacc", "bison -y")
    
def build():
    shelltools.cd("libipsec")
    autotools.make()
    shelltools.cd()
    
    shelltools.cd("setkey")
    autotools.make()
    shelltools.cd()
   
    autotools.make()

    autotools.make("man")
                    
def install():
    pisitools.dobin("setkey/setkey")
    
    pisitools.dobin("ping", "/bin")
    pisitools.dobin("ping6", "/bin")

    pisitools.dosbin("arping", "/sbin")
    
    pisitools.dosbin("tracepath")
    pisitools.dosbin("tracepath6")
    pisitools.dosbin("traceroute6")
    
    pisitools.dosbin("clockdiff")
    pisitools.dosbin("rarpd")
    pisitools.dosbin("rdisc")
    pisitools.dosbin("ipg")
    pisitools.dosbin("tftpd")

    shelltools.chmod(get.installDIR() + "/bin/ping", 04711)
    shelltools.chmod(get.installDIR() + "/bin/ping6", 04711)

    pisitools.dodoc("INSTALL", "RELNOTES")
    
    pisitools.doman("doc/*.8")
