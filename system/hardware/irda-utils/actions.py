#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("WANT_AUTOMAKE", "1.4")
    shelltools.export("RPM_OPT_FLAGS", get.CFLAGS())

def build():
    
    autotools.make("ROOT=\"%s\" RPM_BUILD_ROOT=\"%s\"" % (get.installDIR(), get.installDIR()))

    shelltools.cd("irsockets")
    autotools.make()

    shelltools.cd("../findchip")
    autotools.make("gfindchip")

def install():
    
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/sbin")

    autotools.install("PREFIX=\"%s\" ROOT=\"%s\" MANDIR=\"%s/usr/share/man\"" % (get.installDIR(), get.installDIR(), get.installDIR()))

    # irda-utils's install-etc installs files in /etc/sysconfig if
    # that directory exists on the system, so clean up just in case.
    # This is for bug 1797 (17 Jan 2004 agriffis)
    # rm -rf ${D}/etc/sysconfig 2>/dev/null

    pisitools.dobin("irsockets/irdaspray")
    pisitools.dobin("irsockets/ias_query")
    pisitools.dobin("irsockets/irprintf")
    pisitools.dobin("irsockets/irprintfx")
    pisitools.dobin("irsockets/irscanf")
    pisitools.dobin("irsockets/recv_ultra")
    pisitools.dobin("irsockets/send_ultra")

    pisitools.dosbin("findchip/gfindchip")
    pisitools.dodoc("README")
    pisitools.dodoc("etc/modules.conf.irda")

    # install README's into /usr/share/doc
    for i in ["irattach", "irdadump", "irdaping", "irsockets", "tekram"]:
        pisitools.newdoc(i + "/README", "README." + i)
    

