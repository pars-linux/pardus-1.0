#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("pppd/Makefile.linux", "^#USE_PAM=y", "USE_PAM=y")
    pisitools.dosed("pppd/Makefile.linux", "#HAVE_INET6", "HAVE_INET6")
    pisitools.dosed("pppd/Makefile.linux", "^#CBCP=y", "CBCP=y")
    pisitools.dosed("pppd/plugins/Makefile.linux", "SUBDIRS := rp-pppoe", "SUBDIRS := rp-pppoe radius")
    pisitools.dosed("pppd/plugins/radius/radiusclient/lib/Makefile.in", "^CFLAGS = @CFLAGS@", "CFLAGS = @CFLAGS@ -fPIC")
    pisitools.dosed("pppd/plugins/rp-pppoe/if.c", "net/bpf.h", "pcap-bpf.h")
    pisitools.dosed("pppd/demand.c", "net/bpf.h", "pcap-bpf.h")
    pisitools.dosed("pppd/sys-linux.c", "net/bpf.h", "pcap-bpf.h")
   
    shelltools.export("WANT_AUTOCONF", "2.1")
    libtools.gnuconfig_update()
    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())

    # We must build radius client first
    shelltools.cd("pppd/plugins/radius/radiusclient")
    autotools.configure()
    autotools.make("-j1")

    # and then build the original package
    shelltools.cd("../../../..")
    autotools.rawConfigure("--prefix=/usr")
            
def build():
    autotools.make("COPTS=\"%s\"" % get.CFLAGS())

def install():
    pisitools.doman("chat/chat.8")
    pisitools.dosbin("chat/chat")
    pisitools.doman("pppd/pppd.8")
    pisitools.dosbin("pppd/pppd")
    pisitools.doman("pppdump/pppdump.8")
    pisitools.dosbin("pppdump/pppdump")
    pisitools.doman("pppstats/pppstats.8")
    pisitools.dosbin("pppstats/pppstats")

    shelltools.chmod("%s/usr/sbin/pppd" % get.installDIR(), 4511)

    pisitools.dodir("/etc/ppp/peers")
    pisitools.insinto("/etc/ppp", "etc.ppp/pap-secrets", "pap-secrets.example")
    shelltools.chmod("%s/etc/ppp/pap-secrets.example" % get.installDIR(), 0600)
    pisitools.insinto("/etc/ppp", "etc.ppp/chap-secrets", "chap-secrets.example")
    shelltools.chmod("%s/etc/ppp/chap-secrets.exampl" % get.installDIR(), 0600)

    pisitools.insinto("/etc/ppp", "etc.ppp/options")
    shelltools.chmod("%s/etc/ppp/options" % get.installDIR(), 0644)

    pisitools.insinto("/etc/pam.d", "pppd/ppp.pam", "ppp")
    shelltools.chmod("%s/etc/pam.d/ppp" % get.installDIR(), 0644)

    pisitools.dolib_so("pppd/plugins/minconn.so")
    pisitools.dolib_so("pppd/plugins/passprompt.so")
    pisitools.dolib_so("pppd/plugins/rp-pppoe/rp-pppoe.so")
    pisitools.dolib_so("pppd/plugins/radius/radius.so")
    pisitools.dolib_so("pppd/plugins/radius/radattr.so")
    pisitools.dolib_so("pppd/plugins/radius/radrealms.so")

    pisitools.dodir("/usr/lib/pppd/2.4.2")
    pisitools.domove("/usr/lib/*.so", "/usr/lib/pppd/2.4.2")

    pisitools.dodoc("PLUGINS", "README*", "SETUP", "Changes-2.3", "FAQ")

    pisitools.doman("pppd/plugins/radius/pppd-radius.8")
    pisitools.doman("pppd/plugins/radius/pppd-radattr.8")

    pisitools.dosbin("scripts/pon")
    pisitools.dosbin("scripts/poff")
    pisitools.dosbin("scripts/plog")
    pisitools.doman("scripts/pon.1")

    # Adding misc. specialized scripts to doc dir
    # pisitools.dodir("/usr/share/doc/%s/scripts/chatchat" % get.srcTAG())
    pisitools.insinto("/usr/share/doc/%s/scripts" % get.srcTAG(), "scripts/*")
    # pisitools.insinto("/usr/share/doc/%s/scripts/chatchat" % get.srcTAG(), "scripts/chatchat/*")
    
    # install radiusclient
    shelltools.cd("pppd/plugins/radius/radiusclient")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

