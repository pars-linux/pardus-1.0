#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Don't use zlib from source
    pisitools.removeDir("zlib")
    pisitools.dosed("configure.in", "zlib/Makefile dnl", "dnl zlib/Makefile")

    # Plain autoconf doesn't work here...
    shelltools.export("WANT_AUTOCONF", "2.59")

    autotools.autoreconf("--force")
    libtools.libtoolize("--copy --force")
    libtools.gnuconfig_update()

    shelltools.cd("innobase/")
    autotools.autoreconf("--force")
    libtools.libtoolize("--copy --force")
    libtools.gnuconfig_update()
    shelltools.cd("../")
   
    # Export flags
    shelltools.export("CFLAGS", "%s -DHAVE_ERRNO_AS_DEFINE=1" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s \
                                   -felide-constructors \
                                   -fno-exceptions \
                                   -fno-rtti" % get.CXXFLAGS())

    # Configure!
    autotools.configure("--libexecdir=/usr/sbin \
                         --sysconfdir=/etc/mysql \
                         --localstatedir=/var/lib/mysql \
                         --with-low-memory \
                         --enable-assembler \
                         --enable-local-infile \
                         --with-mysqld-user=mysql \
                         --with-client-ldflags=-lstdc++ \
                         --enable-thread-safe-client \
                         --with-comment=\"Pardus Linux\" \
                         --with-unix-socket-path=/var/run/mysqld/mysqld.sock \
                         --with-zlib-dir=/usr \
                         --with-lib-ccflags=\"-fPIC\" \
                         --with-readline \
                         --enable-shared \
                         --enable-static \
                         --with-openssl \
                         --without-debug \
                         --without-bench \
                         --with-charset=utf8 \
                         --with-collation=utf8_general_ci \
                         --with-extra-charsets=all \
                         --with-berkeley-db=./bdb \
                         --with-big-tables")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s benchdir_root=\"/usr/share/mysql\"" % get.installDIR())

    # Move libs to /usr/lib
    pisitools.domove("/usr/lib/mysql/libmysqlclient*.so*", "/usr/lib")

    # Links to libs
    pisitools.dosym("../libmysqlclient.so", "/usr/lib/mysql/libmysqlclient.so")
    pisitools.dosym("../libmysqlclient_r.so ", "/usr/lib/mysql/libmysqlclient_r.so")

    # Extra headers
    pisitools.insinto("/usr/include/mysql", "include/my_config.h")
    pisitools.insinto("/usr/include/mysql", "include/my_dir.h")

    # Links
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlanalyze")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlrepair")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqloptimize")

    # Cleanup
    pisitools.remove("/usr/bin/make*distribution")
    pisitools.remove("/usr/share/mysql/make_*_distribution")
    pisitools.remove("/usr/share/mysql/mysql.server")
    pisitools.remove("/usr/share/mysql/binary-configur")
    pisitools.remove("/usr/share/mysql/mysql-log-rotate")
    pisitools.remove("/usr/share/mysql/postinstall")
    pisitools.remove("/usr/share/mysql/preinstall")
    pisitools.remove("/usr/share/mysql/mi_test*")
    pisitools.remove("/usr/share/mysql/*.spec")
    pisitools.remove("/usr/share/mysql/*.plist")
    pisitools.remove("/usr/share/mysql/my-*.cnf")

    # No perl
    for i in ["mysqlhotcopy", "mysql_find_rows", "mysql_convert_table_format",
              "mysqld_multi", "mysqlaccess", "mysql_fix_extensions",
              "mysqldumpslow", "mysql_zap", "mysql_explain_log", "mysql_tableinfo",
              "mysql_setpermission"]:
        pisitools.remove("/usr/bin/%s" % i)
    pisitools.removeDir("/usr/share/mysql/sql-bench")

    # No tests
    pisitools.removeDir("/usr/share/mysql/mysql-test")

    # Config
    pisitools.insinto("/etc/mysql", "scripts/mysqlaccess.conf")

    # Data dir
    pisitools.dodir("/var/lib/mysql")

    # Logs
    pisitools.dodir("/var/log/mysql")
    shelltools.touch("%s/var/log/mysql/mysql.log" % get.installDIR())
    shelltools.touch("%s/var/log/mysql/mysql.err" % get.installDIR())

    # Runtime data
    pisitools.dodir("/var/run/mysqld")

    # Documents
    pisitools.dodoc("README", "COPYING", "ChangeLog", "EXCEPTIONS-CLIENT", "INSTALL-SOURCE")
    pisitools.dohtml("Docs/*.html")
    pisitools.dodoc("Docs/manual.txt," "Docs/manual.ps")
    pisitools.dodoc("support-files/my-*.cnf")
