#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("saslauthd/auth_rimap.c", "(?m)^(define DEFAULT_REMOTE_SERVICE.*)imap", r"\1 imap2")

    shelltools.export("WANT_AUTOCONF", "2.5")
    
    pisitools.remove("configure")
    pisitools.remove("config.h.in")
    pisitools.remove("autom4te.cache")
    
    autotools.aclocal("-I cmulocal -I config")
    autotools.autoheader()
    autotools.autoconf()

    autotools.configure("--with-saslauthd=/var/lib/sasl2 \
                        --with-pwcheck=/var/lib/sasl2  \
                        --with-configdir=/etc/sasl2 \
                        --with-plugindir=/usr/lib/sasl2 \
                        --with-dbpath=/etc/sasl2/sasldb2 \
                        --enable-login \
                        --enable-ntlm \
                        --disable-krb4 \
                        --disable-otp \
                        --disable-static \
                        --with-openssl \
                        --with-pam \
                        --without-ldap \
                        --disable-gssapi \
                        --without-mysql \
                        --disable-mysql \
                        --without-pgsql \
                        --disable-postgres \
                        --disable-java \
                        --without-authdaemond \
                        --disable-sql \
                        --with-dblib=gdbm")

def build():
    # Parallel build doesn't work.
    autotools.make("-j1")
    
    shelltools.cd("saslauthd/")

    autotools.make("testsaslauthd")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/sasl2")

    # boş sasldb2 veritabanı additional file olarak pspec içerisine eklendi..

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "doc/TODO", "doc/*.txt")
    pisitools.dohtml("doc/*.html")

    for doc in ["AUTHORS", "COPYING", "ChangeLog", "LDAP_SASLAUTHD", "NEWS", "README"]:
        pisitools.newdoc("saslauthd/%s" % doc, "saslauthd/%s" % doc)
