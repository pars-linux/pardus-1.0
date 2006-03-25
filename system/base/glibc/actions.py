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

NoStrip = ["/lib/libpthread-2.3.5.so", "/lib/libthread_db-1.0.so"]
WorkDir = "glibc-2.3.5"

def undef_variables():
    shelltools.export("LANGUAGE","C") 
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C") 
    shelltools.export("LD_RUN_PATH","")

def setup_locales():
    # These should not be set, else the zoneinfo do not always get installed ...
    undef_variables()

    shelltools.cd("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())
    autotools.rawInstall("PARALLELMFLAGS=${MAKEOPTS} -j1 install_root=%s localedata/install-locales" % get.installDIR())

def setup():
    shelltools.chmod("scripts/*.sh")

    undef_variables()

    conf = "--disable-dev-erandom \
            --with-tls \
            --with-__thread \
            --enable-add-ons=nptl,c_stubs,glibc-compat,libidn \
            --enable-kernel=2.6.5 \
            --without-cvs \
            --enable-bind-now \
            --build=%s \
            --host=%s \
            --disable-profile \
            --without-gd \
            --with-headers=/usr/include \
            --prefix=/usr \
            --mandir=/usr/share/man \
            --infodir=/usr/share/info \
            --libexecdir=/usr/lib/misc" % (get.HOST(), get.HOST())

    shelltools.makedirs("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())
    shelltools.cd("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())
    shelltools.system("%s/%s/configure %s" % (get.workDIR(), WorkDir, conf))
        
def build():
    shelltools.cd("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())
    autotools.make()

def install():
    # These should not be set, else the zoneinfo do not always get installed ...
    undef_variables()
    
    shelltools.cd("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())
    autotools.rawInstall("PARALLELMFLAGS=${MAKEOPTS} install_root=%s" % get.installDIR())

    # Some things want this, notably ash.
    pisitools.dosym("libbsd-compat.a", "/usr/lib/libbsd.a")

    # install glibc-info
    autotools.rawInstall("PARALLELMFLAGS=${MAKEOPTS} install_root=%s info -i" % get.installDIR())

    setup_locales()

    # We'll take care of the cache ourselves
    pisitools.remove("/etc/ld.so.cache")

    # FIXME: man pages included as patch so install them
    # pisitools.dodir("/usr/share/man/man3")
    # pisitools.doman("/man/*.3thr")

    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "FAQ", "INTERFACE", "NEWS", "NOTES", "PROJECTS", "README*")

    # Is this next line actually needed or does the makefile get it right?
    # It previously has 0755 perms which was killing things.
    shelltools.chmod("%s/usr/lib/misc/pt_chown" % get.installDIR(), 04711)

    # Prevent overwriting of the /etc/localtime symlink.  
    pisitools.remove("/etc/localtime")
