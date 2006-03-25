#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Configure", "-O3 -fomit-frame-pointer -m486 -Wall", "%s -Wall" % get.CFLAGS())
    pisitools.dosed("Configure", "-O3 -fomit-frame-pointer -mcpu=pentium -Wall", "%s -Wall" % get.CFLAGS())
    pisitools.dosed("Configure", "-O3 -fomit-frame-pointer -mcpu=pentiumpro -Wall", "%s -Wall" % get.CFLAGS())
    shelltools.system("./config --prefix=/usr --openssldir=/etc/ssl shared threads -Wa,--noexecstack")
    
def build():
    autotools.make("all")

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())
    pisitools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
    pisitools.dohtml("doc/*")

    # create the certs directory.  
    pisitools.insinto("/etc/ssl/certs/", "certs/*.pem")
    shelltools.system("OPENSSL=%s/usr/bin/openssl /usr/bin/perl tools/c_rehash %s/etc/ssl/certs" % (get.installDIR(), get.installDIR()))

    # The man pages rand.3 and passwd.1 conflict with other packages
    # Rename them to ssl-* and also make a symlink from openssl-* to ssl-*
    pisitools.domove("/usr/share/man/man1/passwd.1", "/usr/share/man/man1/", "ssl-passwd.1")
    pisitools.dosym("ssl-passwd.1", "/usr/share/man/man1/openssl-passwd.1")

    pisitools.domove("/usr/share/man/man3/rand.3", "/usr/share/man/man3/", "ssl-rand.3")
    pisitools.dosym("ssl-rand.3", "/usr/share/man/man3/openssl-rand.3")
 
    shelltools.chmod("%s/usr/lib/pkgconfig" % get.installDIR())
