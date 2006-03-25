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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "Linux-PAM-0.77" 

def setup():
    shelltools.copy("/usr/share/automake/install-sh", ".")
    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.autoconf()
    
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.rawConfigure("./configure --libdir=/lib \
                           --enable-static-libpam \
                           --enable-fakeroot=%s \
                           --enable-isadir=/lib/security \
                           --host=%s" % (get.installDIR(), get.HOST()))

    # Python stuff in docs gives sandbox problems
    pisitools.dosed("Makefile", "modules doc examples", "modules")

    # Do not build pam_userdb.so ...
    pisitools.dosed("Make.Rules", "^HAVE_NDBM_H=yes", "HAVE_NDBM_H=no")
    pisitools.dosed("Make.Rules", "^HAVE_LIBNDBM=yes" ,"HAVE_LIBNDBM=no")
    pisitools.dosed("Make.Rules", "^HAVE_LIBDB=yes", "HAVE_LIBDB=no")

   # Also edit the configuration file else the wrong include files get used
    pisitools.dosed("_pam_aconf.h", "^#define HAVE_NDBM_H.*$", "/* #undef HAVE_NDBM_H */")
    pisitools.dosed("_pam_aconf.h", "^#define HAVE_DB_H.*$", "/* #undef HAVE_DB_H */")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("FAKEROOT=%s  LDCONFIG=\"\"" % get.installDIR())

    for file in ("pam", "pamc", "pam_misc"):
        pisitools.remove("/lib/lib%s.so" % file)
        pisitools.dosym("lib%s.so.0.77" % file, "/lib/lib%s.so" % file)
        pisitools.dosym("lib%s.so.0.77" % file, "/lib/lib%s.so.0" % file)
        pisitools.domove("/lib/lib%s.a" % file, "/usr/lib/")
        libtools.gen_usr_ldscript("lib%s.so" % file)

    pisitools.doman("doc/man/*.[0-9]")

    pisitools.dodoc("CHANGELOG", "Copyright", "README")
#    docinto modules ; dodoc modules/README ; dodoc doc/txts/README.*
#    docinto txt ; dodoc doc/specs/*.txt #doc/txts/*.txt

    # need this for pam_console
    pisitools.dodir("/var/run/console")
