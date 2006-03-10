#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

libpath = "/usr/lib/binutils/%s/%s" % (get.HOST(), get.srcVERSION())
incpath = libpath + "/include"
binpath = "/usr/%s/binutils-bin/%s" % (get.HOST(), get.srcVERSION())
datapath = "/usr/share/binutils-data/%s/%s" % (get.HOST(), get.srcVERSION())

def setup():
    for dir in ["bfd/po", "binutils/po", "gas/po", "gprof/po", "ld/po", "opcodes/po"]:
        pisitools.dosed("%s/Make-in" % dir, "(?m)^(datadir = )$(prefix)/@DATADIRNAME@", r"@datadir@")
        pisitools.dosed("%s/Make-in" % dir, "(?m)^(gnulocaledir = )$(prefix)/share", r"$(datadir)")

    libtools.gnuconfig_update()
    libtools.libtoolize("--copy --force") 

    config_parameter = "--without-included-gettext \
                         --disable-nls \
                         --host=%s \
                         --target=%s\
                         --datadir=%s \
                         --infodir=%s/info \
                         --mandir=%s/man \
                         --bindir=%s \
                         --libdir=%s \
                         --libexecdir=%s \
                         --includedir=%s \
                         --enable-shared \
                         --disable-werror" % (get.HOST(), get.HOST(), datapath, datapath,\
                                          datapath, binpath, libpath, libpath, incpath)

    autotools.rawConfigure(config_parameter)

def build():
    autotools.make("-j1 configure-bfd")
    autotools.make("-j1 headers -C bfd")
    autotools.make("all")
    autotools.make("info")
    
def install():
    autotools.rawInstall("DESTDIR=%s tooldir=%s" % (get.installDIR(), libpath))

    pisitools.removeDir("%s/bin" % libpath)
    pisitools.insinto(incpath, "include/libiberty.h")
    pisitools.domove("%s/lib/ldscripts/" % libpath, "%s/ldscripts" % libpath)
    pisitools.removeDir(libpath + "/lib")

    pisitools.dodir("/usr/%s/lib" % get.HOST())

    pisitools.dodoc("README")

    bins = ["addr2line", "ar", "as", "c++filt", "gprof", "ld", "nm", \
            "objcopy", "objdump", "ranlib", "readelf", "size", "strings", "strip"]

    libs = ["ldscripts", "libbfd-%s.so" % get.srcVERSION(),  "libbfd.a", "libbfd.la",  "libbfd.so", \
             "libiberty.a", "libopcodes-%s.so" % get.srcVERSION(),  "libopcodes.a",  "libopcodes.la",  "libopcodes.so"]

    for bin in bins: 
        pisitools.dosym("/usr/%s/binutils-bin/%s/%s" % (get.HOST(), get.srcVERSION(), bin), \
                        "/usr/bin/%s-%s" % (get.HOST(), bin))

        pisitools.dosym("%s-%s" % (get.HOST(), bin), \
                        "/usr/bin/%s" % (bin))

    for lib in libs:
        pisitools.dosym("/usr/lib/binutils/%s/%s/%s" % (get.HOST(), get.srcVERSION(), lib), \
                        "/usr/%s/lib/%s" % (get.HOST(), lib))
    
    for d in ["0001", "0203", "9193", "9495", "9697", "9899"]:
        pisitools.newdoc("bfd/ChangeLog-%s" % d, "bfd/ChangeLog-%s" % d) 
    for d in ["0001", "0203", "9295", "9697", "9899"]:
        pisitools.newdoc("gas/ChangeLog-%s" % d, "gas/ChangeLog-%s" % d) 
    for d in ["", "-0001", "-0203", "-9197", "-9899", ".linux"]:
        pisitools.newdoc("ld/ChangeLog%s" % d, "ld/ChangeLog%s" % d)
    for d in ["", "-0001", "-0203", "-9297", "-9899", ".linux"]:
        pisitools.newdoc("opcodes/ChangeLog%s" % d, "opcodes/ChangeLog%s" % d)
        
    pisitools.newdoc("bfd/README", "bfd/README") 
    pisitools.newdoc("bfd/PORTING", "bfd/PORTING") 
    pisitools.newdoc("bfd/TODO", "bfd/TODO") 
    pisitools.newdoc("binutils/ChangeLog", "binutils/ChangeLog") 
    pisitools.newdoc("binutils/NEWS", "binutils/NEWS") 
    pisitools.newdoc("binutils/README", "binutils/README") 
    pisitools.newdoc("gas/CONTRIBUTORS", "gas/CONTRIBUTORS") 
    pisitools.newdoc("gas/NEWS", "gas/NEWS") 
    pisitools.newdoc("gas/README", "gas/README") 
    pisitools.newdoc("gas/README-vms", "gas/README-vms")
    pisitools.newdoc("gprof/ChangeLog", "gprof/ChangeLog") 
    pisitools.newdoc("gprof/ChangeLog.linux", "gprof/ChangeLog.linux") 
    pisitools.newdoc("gprof/ChangeLog-9203", "gprof/ChangeLog-9203")
    pisitools.newdoc("gprof/TEST", "gprof/TEST")
    pisitools.newdoc("gprof/TODO", "gprof/TODO")
    pisitools.newdoc("gprof/bbconv.pl", "gprof/bbconv.pl")
    pisitools.newdoc("ld/README", "ld/README")
    pisitools.newdoc("ld/NEWS", "ld/NEWS")  
    pisitools.newdoc("ld/TODO", "ld/TODO")
    pisitools.newdoc("libiberty/ChangeLog.linux", "libiberty/ChangeLog.linux")
    pisitools.newdoc("libiberty/ChangeLog", "libiberty/ChangeLog")
    pisitools.newdoc("libiberty/README", "libiberty/README")
