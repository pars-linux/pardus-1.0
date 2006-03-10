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
    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.autoconf()
    
    autotools.configure("--with-cups-user=lp \
                        --with-cups-group=lp \
                        --localstatedir=/var \
                        --enable-pam \
                        --enable-ssl \
                        --enable-slp \
                        --enable-nls \
                        --enable-openssl")

def build():
    autotools.make()

def install():
    pisitools.dodir("/var/spool")
    pisitools.dodir("/var/log/cups")
    pisitools.dodir("/etc/cups")

    args ="LOCALEDIR=%(installDIR)s/usr/share/locale \
           DOCDIR=%(installDIR)s/usr/share/cups/docs \
           REQUESTS=%(installDIR)s/var/spool/cups \
           SERVERBIN=%(installDIR)s/usr/lib/cups \
           DATADIR=%(installDIR)s/usr/share/cups \
           INCLUDEDIR=%(installDIR)s/usr/include \
           AMANDIR=%(installDIR)s/usr/share/man \
           PMANDIR=%(installDIR)s/usr/share/man \
           MANDIR=%(installDIR)s/usr/share/man \
           SERVERROOT=%(installDIR)s/etc/cups \
           LOGDIR=%(installDIR)s/var/log/cups \
           SBINDIR=%(installDIR)s/usr/sbin \
           PAMDIR=%(installDIR)s/etc/pam.d \
           EXEC_PREFIX=%(installDIR)s/usr \
           LIBDIR=%(installDIR)s/usr/lib \
           BINDIR=%(installDIR)s/usr/bin \
           bindir=%(installDIR)s/usr/bin \
           INITDIR=%(installDIR)s/etc \
           PREFIX=%(installDIR)s" % {'installDIR': get.installDIR()}

    autotools.rawInstall(args)

    pisitools.dodoc("CHANGES.txt", "CREDITS.txt", "ENCRYPTION.txt", "LICENSE.txt", "README.txt")

    pisitools.dosym("/usr/share/cups/docs", "/usr/share/doc/%s/html" % get.srcTAG())

    # cleanups
    pisitools.removeDir("/etc/init.d")
    pisitools.removeDir("/etc/pam.d")
    pisitools.removeDir("/etc/rc*")
    pisitools.removeDir("/usr/share/man/cat*")
    pisitools.removeDir("/etc/cups/certs")
    pisitools.removeDir("/etc/cups/interfaces")
    pisitools.removeDir("/etc/cups/ppd")
    pisitools.removeDir("/var")

    pisitools.dosed("%s/etc/cups/cupsd.conf" % get.installDIR(), "^#\(DocumentRoot\).*", "\1 /usr/share/cups/docs")
    pisitools.dosed("%s/etc/cups/cupsd.conf" % get.installDIR(), "^#\(SystemGroup\).*", "\1 lp")
    pisitools.dosed("%s/etc/cups/cupsd.conf" % get.installDIR(), "^#\(User\).*", "\1 lp")
    pisitools.dosed("%s/etc/cups/cupsd.conf" % get.installDIR(), "^#\(Group\).*", "\1 lp")

    # allow raw printing
    pisitools.dosed("%s/etc/cups/mime.types" % get.installDIR(), "#application/octet-stream", "application/octet-stream")

    # fix #691
    pisitools.dosym("/usr/share/cups/docs", "/usr/share/doc/cups")
    
    # cleanup
    pisitools.remove("/usr/share/cups/docs/*.pdf")
    
    pisitools.removeDir("/usr/share/cups/docs/be")
    pisitools.removeDir("/usr/share/cups/docs/de")
    pisitools.removeDir("/usr/share/cups/docs/es")
    pisitools.removeDir("/usr/share/cups/docs/fr")
