#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "lirc-0.8.0pre1"

def setup():
    # filter-flags -Wl,-O1
    pisitools.dosed("configure", "-O2 -g", get.CFLAGS())
    pisitools.dosed("configure.in", "-O2 -g", get.CFLAGS())

    # fix bz878 compilation
    pisitools.dosed("configure", "lircd.conf.pixelview_bt878", "lircd.conf.playtv_bt878")
    pisitools.dosed("configure.in", "lircd.conf.pixelview_bt878", "lircd.conf.playtv_bt878")

   
    # Patch bad configure for /usr/src/linux
    libtools.libtoolize("--copy --force")
    
    pisitools.dosed("acinclude.m4", "/usr/src/kernel\-source\-\`uname \-r\` /usr/src/linux\-\`uname \-r\`")
    pisitools.dosed("aclocal.m4", "/usr/src/kernel\-source\-\`uname \-r\` /usr/src/linux\-\`uname \-r\`")
    pisitools.dosed("configure", "/usr/src/kernel\-source\-\`uname \-r\` /usr/src/linux\-\`uname \-r\`")

    pisitools.dosed("configure", "\`uname \-r\`", get.curKERNEL())
    pisitools.dosed("configure.in", "\`uname \-r\`", get.curKERNEL())
    pisitools.dosed("setup.sh", "\`uname \-r\`", get.curKERNEL())

    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.configure("--disable-manage-devices \
                         --localstatedir=/var \
                         --with-syslog=LOG_DAEMON \
                         --enable-sandboxed \
                         --with-x \
                         --with-driver=any \
                         --with-kerneldir=%s/usr/src/linux \
                         --with-moduledir=%s/lib/modules/linux-%s/extra" % (get.installDIR(), get.installDIR(), get.curKERNEL()))

def build():
    # remove parallel port driver if using an SMP system
    # pisitools.dosed("drivers/Makefile", "lirc_parallel", "")

    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # we use udev
    pisitools.insinto("/etc/udev/rules.d", "contrib/lirc.rules", "10-lirc.rules")

    pisitools.dohtml("doc/html/*.html")
    pisitools.insinto("/usr/share/doc/%s/images" % get.srcTAG(), "doc/images/*")

