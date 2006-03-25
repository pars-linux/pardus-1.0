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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.cd("mDNSPosix/")
    autotools.make("os=linux")

def install():
    shelltools.cd("mDNSPosix/")

    pisitools.dodir("/usr/sbin")
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include")
    pisitools.dodir("/lib/")
    pisitools.dodir("/etc/")
    pisitools.dodir("/usr/share/man/man5/")
    pisitools.dodir("/usr/share/man/man8/")

    autotools.rawInstall("DESTDIR=%s/ os=linux" % get.installDIR()) 

    pisitools.dosbin("build/prod/dnsextd")
    pisitools.dosbin("build/prod/mDNSResponderPosix")
    pisitools.dosbin("build/prod/mDNSNetMonitor")

    pisitools.dobin("../Clients/build/dns-sd")
    pisitools.dobin("build/prod/mDNSProxyResponderPosix")
    pisitools.dobin("build/prod/mDNSIdentify")
