#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.gnuconfig_update()
    libtools.libtoolize("--copy --force")

    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS()) 

    parameters = "--disable-desrpc \
                  --with-libcrypt \
                  --with-libcrack \
                  --enable-shared=no \
                  --enable-static=yes \
                  --with-libpam \
                  --without-libskey \
                  --without-selinux \
                  --enable-nls"

    autotools.configure(parameters)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod(get.installDIR() + "/bin/su", 04711)

    for file in ["chfn", "chsh", "chage", "expiry", "newgrp", "passwd", "gpasswd"]:
        shelltools.chmod("%s/usr/bin/%s" % (get.installDIR(), file), 04711)

    for extension in ["a", "la"]:
        for file in ["libshadow"]:
            pisitools.remove("/lib/%s.%s" % (file, extension))

    pisitools.remove("/bin/login") #we're using pam..

    pisitools.insinto("/etc/", "etc/login.access")
    shelltools.chmod("%s/etc/login.access" % get.installDIR(), 0600)

    pisitools.insinto("/etc/", "etc/limits")
    shelltools.chmod("%s/etc/limits" % get.installDIR(), 0644)

    pisitools.domove("/usr/bin/passwd", "/bin/")
    pisitools.dosym("/bin/passwd", "/usr/bin/passwd")

    pisitools.remove("/usr/share/man/cs/man1/id.1")
    
    for directory in ["", "cs", "fr", "it", "ja", "ko", "pl", "ru"]:
        pisitools.remove("/usr/share/man/%s/man5/passwd.5" % directory)
    
    pisitools.remove("/usr/share/man/man3/getspnam.3")

    pisitools.dodoc("doc/INSTALL", "doc/README", "doc/WISHLIST")
    pisitools.dodir("/usr/share/doc/%s/txt" % get.srcTAG())

    newDocPrefix = "%s/usr/share/doc/%s" % (get.installDIR(), get.srcTAG())
    pisitools.newdoc("doc/HOWTO", "%s/txt/HOWTO" % newDocPrefix)
    pisitools.newdoc("doc/LSM", "%s/txt/LSM" % newDocPrefix)
    
    for file in ["", ".linux", ".limits", ".mirrors", ".nls", ".pam", ".platforms", ".sun4"]:
        pisitools.newdoc("doc/README%s" % file, "%s/txt/README%s" % (newDocPrefix, file))
        
    pisitools.newdoc("doc/console.c.spec.txt", "%s/txt/console.c.spec.txt" % newDocPrefix)
