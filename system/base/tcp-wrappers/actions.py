# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Timu EREN <selamtux@gmail.com>
#

# Not : Makefile.Pardus yaması actions.py
# dosyasının pspec.xml dosyasında belirtilen yamaların
# uygulandıktan sonra işletilmesi nedeni ile dahil edilmiştir.
# daha sonraki paketleyiciler için yamayı oluşturmak için
# kullanılan sed ifadesi şu şekildedir.
# sed -i -e "s:-O:\${PARDUS_CFLAGS}:" -e "s:AUX_OBJ=.*:AUX_OBJ= \\\:" Makefile
# Daha sonraki versiyonu paketlerken MINOR, REL ve WorkDir değişkenlerini
# sürüme göre değiştirmeyi unutmayın.


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "tcp_wrappers_7.6"

def setup():
    shelltools.chmod("Makefile", 0755)
    pisitools.dosed("Makefile", "@make", "@$(MAKE) ")
    pisitools.dosed("Makefile", "make;", "$(MAKE);")

def build():
    MINOR = "7"
    REL = "6"

    shelltools.export("PARDUS_CFLAGS", "%s" % get.CFLAGS())

    args = "REAL_DAEMON_DIR=%s \
            PARDUS_OPT=\"-DINET6=1 -Dss_family=__ss_family -Dss_len=__ss_len\" \
            MAJOR=0 MINOR=%s REL=%s" % ( get.sbinDIR(), MINOR, REL )
    
    autotools.make("%s config-check" % args)
    autotools.make("%s linux" % args)

def install():
    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.allow.5")
    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.deny.5")

    pisitools.dosbin("tcpd")
    pisitools.dosbin("tcpdchk")
    pisitools.dosbin("tcpdmatch")
    pisitools.dosbin("safe_finger")
    pisitools.dosbin("try-from")
    
    pisitools.doman("*.3", "*.5", "*.8")
    
    pisitools.insinto("/usr/include/", "tcpd.h")

    pisitools.dolib_a("libwrap.a")
    
    pisitools.domove("libwrap.so", "libwrap.so.0.%s" % get.srcVERSION())
    pisitools.dolib_so("libwrap.so.0.%s" % get.srcVERSION(), "/lib")
    
    pisitools.dosym("/lib/libwrap.so.0.%s" % get.srcVERSION(), "/lib/libwrap.so.0")
    pisitools.dosym("/lib/libwrap.so.0", "/lib/libwrap.so")
    
    libtools.gen_usr_ldscript("libwrap.so")

    pisitools.dodoc("BLURB", "CHANGES", "DISCLAIMER", "README*", "hosts.allow.example")
