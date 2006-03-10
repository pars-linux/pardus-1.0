#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.echo("#define VSF_BUILD_TCPWRAPPERS", "builddefs.h")
    shelltools.echo("#define VSF_BUILD_SSL", "builddefs.h")
                    
def build():
    autotools.make("CFLAGS=\"%s\"" % get.CFLAGS())

def install():
    pisitools.dosbin("vsftpd")
    
    pisitools.dodoc("AUDIT", "BENCHMARKS", "BUGS", "Changelog", "FAQ", "INSTALL", "LICENSE", "README", "README.security", "REWARD", "SIZE", "SPEED", "TODO", "TUNING")
    pisitools.newdoc("vsftpd.conf", "vsftpd.conf.example")
    pisitools.doman("vsftpd.conf.5", "vsftpd.8")

    pisitools.dodir("/home/ftp")
    pisitools.dodir("/home/ftp/incoming")
    shelltools.chown("%s/home/ftp/incoming" % get.installDIR( ), "ftp", "ftp")

    pisitools.dodir("/usr/share/vsftpd/empty")
