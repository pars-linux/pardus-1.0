#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@haftalik.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="cdrtools-2.01.01"

def setup():
    pisitools.dosed("DEFAULTS/Defaults.linux", "/opt/schily", "/usr")
    pisitools.dosed("DEFAULTS/Defaults.linux", "/usr/src/linux/include")
    pisitools.dosed("librscg/scsi-remote.c", "/opt/schily", "/usr")

def build():
    autotools.gnuconfig_update()
    autotools.make("CC=\"%s -D__attribute_const__=const\" COPTX=\"%s\" CPPOPTX=\"%s\" LDOPTX=\"%s\"" % (get.CC(), get.CFLAGS(), get.CXXFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dobin("cdda2wav/OBJ/*/cdda2wav")
    pisitools.dobin("cdrecord/OBJ/*/cdrecord")
    pisitools.dobin("mkisofs/OBJ/*/mkisofs")
    pisitools.dobin("readcd/OBJ/*/readcd")
    pisitools.dobin("rscsi/OBJ/*/rscsi")

    pisitools.insinto("/usr/include", "incs/*/align.h")
    pisitools.insinto("/usr/include", "incs/*/avoffset.h")
    pisitools.insinto("/usr/include", "incs/*/xconfig.h")

    pisitools.dobin("sofs/diag/OBJ/*/devdump")
    pisitools.dobin("sofs/diag/OBJ/*/isodump")
    pisitools.dobin("sofs/diag/OBJ/*/isoinfo")
    pisitools.dobin("sofs/diag/OBJ/*/isovfy")

    pisitools.insinto("/etc/default", "rscsi/rscsi.dfl")
    pisitools.insinto("/etc/default", "cdrecord/cdrecord.dfl")

    pisitools.dolib_a("libs/*/*.a")

    pisitools.insinto("/usr/include/scsilib", "include/*.h")
    pisitools.insinto("/usr/include/scsilib/scg", "include/sch/*.h")

    pisitools.dodoc("ABOUT", "Changelog", "README*", "START", "doc/*.ps")
    pisitools.doman("*/*.1", "*/*.8")
