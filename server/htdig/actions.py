#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("CPPFLAGS","-Wno-deprecated")

    autotools.rawConfigure("--prefix=/usr \
                            --enable-shared \
                            --enable-bigfile \
                            --with-config-dir=/etc/htdig \
                            --with-default-config-file=/etc/htdig/htdig.conf \
                            --with-database-dir=/var/lib/htdig \
                            --localstatedir=/var/lib/htdig \
                            --with-common-dir=/usr/share/htdig \
                            --with-cgi-bin-dir=/usr/libexec/htdig/ \
                            --with-image-dir=/usr/share/htdig \
                            --with-search-dir=/usr/share/htdig \
                            --with-zlib=/usr")
    
def build():
    autotools.make()
    
def install():
    dir = get.installDIR()
    autotools.install("DESTDIR=%s \
                       CONFIG_DIR=%s/etc/htdig \
                       SEARCH_DIR=%s/usr/share/htdig \
                       CGIBIN_DIR=%s/var/www/localhost/cgi-bin/ \
                       COMMON_DIR=%s/usr/share/htdig \
                       DATABASE_DIR=%s/var/lib/htdig \
                       IMAGE_DIR=%s/usr/share/htdig \
                       DEFAULT_CONFIG_FILE=%s/etc/htdig/htdig.conf \
                       exec_prefix=%s/usr" % (dir,dir,dir,dir,dir,dir,dir,dir,dir))

    shelltools.chmod("%s/usr/share/htdig/*" % get.installDIR(), 644)
   
    pisitools.dosym("/usr/share/htdig/search.html", "/usr/share/htdig/index.html")
    pisitools.dosym("/usr/libexec/htdig/htsearch", "/usr/bin/htsearch")

    pisitools.dosed("%s/etc/htdig/htdig.conf" % get.installDIR(), get.installDIR())
    pisitools.dosed("%s/usr/bin/rundig" % get.installDIR(), get.installDIR())

