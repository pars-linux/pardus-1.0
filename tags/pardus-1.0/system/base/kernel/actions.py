#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "linux-2.6.14.4"
NoStrip = "/"

def setup():
    # Branding
    pisitools.dosed("Makefile", "EXTRAVERSION = .4", "EXTRAVERSION = .4-%s" % get.srcRELEASE())
    autotools.make("oldconfig")

    # Embed splash-theme into kernel
    shelltools.system("/usr/bin/splash_geninitramfs -v -g usr/initramfs_data.cpio.gz -r 1024x768 pardus")
    
def build():
    autotools.make()

def install():
    suffix = "%s-%s" % (get.srcVERSION(), get.srcRELEASE())

    autotools.rawInstall("INSTALL_MOD_PATH=%s/" % get.installDIR(), "modules_install")

    # remove wrong symlinks
    pisitools.remove("/lib/modules/%s/source" % suffix)
    pisitools.remove("/lib/modules/%s/build" % suffix)

    # create symlinks
    pisitools.dosym("/usr/src/linux-%s/" % suffix, "/lib/modules/%s/source" % suffix)
    pisitools.dosym("/usr/src/linux-%s/" % suffix, "/lib/modules/%s/build" % suffix)

    pisitools.insinto("/boot/", "System.map", "System.map-%s" % suffix)
    pisitools.insinto("/boot/", "arch/i386/boot/bzImage", "kernel-%s" % suffix)

    # prepare kernel for module compiliation
    autotools.make("clean")
    autotools.make("modules_prepare")
    
    # cp source to installDIR for kernel-source package
    pisitools.dodir("/usr/src")
    shelltools.copytree("../linux-%s/" % get.srcVERSION(), "%s/usr/src/linux-%s/" % (get.installDIR(), suffix))
    pisitools.dosym("/usr/src/linux-%s/" % suffix, "linux")
