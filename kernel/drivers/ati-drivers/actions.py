#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

def getCommonDir():
    return "%s/common" % get.workDIR()

def setup():
    shelltools.system("sh ati-driver-installer-8.20.8-i386.run --extract .")

def build():
    CommonDir = getCommonDir()

    shelltools.cd(CommonDir + "/lib/modules/fglrx/build_mod")

    src = "%s/x690/lib/modules/fglrx/build_mod/libfglrx_ip.a.GCC3" % get.workDIR()
    shelltools.sym(src, "libfglrx_ip.a.GCC3")
    
    shelltools.system("sh make.sh")

def install():
    shelltools.cd(getCommonDir())

    install_dir = get.installDIR()

    DIRS = {"etc": "etc",
            "usr/X11R6/include": "usr/include",
            "usr/X11R6/bin": "usr/bin",
            "usr/X11R6/lib": "usr/lib",
            "usr/include/GL/": "usr/include/GL/",
            "usr/share": "usr/share"}

    pisitools.dodir("/usr")
    for source in DIRS:
        target = DIRS[source]
        shelltools.copy(source, "%s/%s" %(install_dir, target))

    pisitools.insinto("/usr/bin", "../x690/usr/X11R6/bin/*")
    pisitools.insinto("/usr/lib", "../x690/usr/X11R6/lib/*")


    pisitools.dosym("/usr/lib/libfglrx_pp.so.1.0", "/usr/lib/libfglrx_pp.1")
    pisitools.dosym("/usr/lib/libfglrx_gamma.so.1.0", "/usr/lib/libfglrx_gamma.1")


    # copy compiled kernel module
    pisitools.dodir("/lib/modules/%s/kernel/drivers/char/drm" % get.curKERNEL())
    pisitools.dodir("/lib/modules/%s/video" % get.curKERNEL())

    import os
    print os.getcwd()
    shelltools.copy("lib/modules/fglrx/fglrx.%s.ko" % get.curKERNEL(),
                    "%s/lib/modules/%s/kernel/drivers/char/drm/fglrx.ko" %(install_dir, get.curKERNEL()))
    shelltools.copy("lib/modules/fglrx/fglrx_agp.%s.ko" % get.curKERNEL(),
                    "%s/lib/modules/%s/video/fglrx_agp.ko" %(install_dir, get.curKERNEL()))

