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

def setup():
    pisitools.dosed("mpi/i386/mpih-add1.S", "PIC", "__PIC__")
    pisitools.dosed("mpi/i386/mpih-sub1.S", "PIC", "__PIC__")
    pisitools.dosed("intl/relocatable.c", "PIC", "__PIC__")

    autotools.configure("--disable-ldap \
                        --enable-mailto \
                        --enable-hkp \
                        --enable-finger \
                        --with-libcurl \
                        --enable-nls \
                        --enable-bzip2 \
                        --enable-card-support \
                        --with-capabilities \
                        --with-readline \
                        --enable-static-rnd=linux \
                        --libexecdir=/usr/libexec \
                        --enable-sha51")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s libexecdir=\"/usr/libexec/gnupg\"" % get.installDIR())

    # caps support makes life easier
    shelltools.chmod("%s/usr/bin/gpg" % get.installDIR(), 04755)

    # keep the documentation in /usr/share/doc/...
    pisitools.remove("/usr/share/gnupg/FAQ")
    pisitools.remove("/usr/share/gnupg/faq.html")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "INSTALL", "NEWS", "PROJECTS", "README", "THANKS", \
                    "TODO", "VERSION", "doc/FAQ" ,"doc/HACKING", "doc/DETAILS", "doc/ChangeLog", "doc/OpenPGP", "doc/faq.raw")
    pisitools.insinto("/usr/share/doc/%s/html" % get.srcTAG(), "doc/faq.html")
