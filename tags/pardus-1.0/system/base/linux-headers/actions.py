#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "linux-2.6.8.1"

#    Stays here for future works ( like Pardus PPC :P )

#    Fixes ... all the mv magic is to keep sed from dumping
#    ugly warnings about how it can't work on a directory.

#    cd "${S}"/include
#    mv asm-ia64/sn asm-ppc64/iSeries .
#    headers___fix asm-ia64/*
#    mv sn asm-ia64/
#    headers___fix asm-ppc64/*
#    mv iSeries asm-ppc64/
#    headers___fix asm-ppc64/iSeries/*
#    headers___fix linux/ethtool.h

#headers___fix() {
#        Voodoo to partially fix broken upstream headers.
#        sed -i \
#            -e "s/\([ "$'\t'"]\)\(u\|s\)\(8\|16\|32\|64\)\([ "$'\t'"]\)/\1__\2\3\4/g;" \
#            -e 's/ \(u\|s\)\(8\|16\|32\|64\)$/ __\1\2/g' \
#            -e 's/\([(, ]\)\(u\|s\)64\([, )]\)/\1__\264\3/g' \
#            -e "s/^\(u\|s\)\(8\|16\|32\|64\)\([ "$'\t'"]\)/__\1\2\3/g;" \
#            "$@"
#}
    
def build():
    shelltools.touch("include/linux/autoconf.h")
    shelltools.sym("asm-i386", "include/asm")

    shelltools.export("HOSTCFLAGS", "-Wall -Wstrict-prototypes -O2 -fomit-frame-pointer -Iinclude/")
    shelltools.export("MOPT", "ARCH=i386 CROSS_COMPILE=i686-pc-linux-gnu-")
                      
    autotools.make("defconfig HOSTCFLAGS=\"${HOSTCFLAGS}\" ${MOPT}")
    
    autotools.make("prepare HOSTCFLAGS=\"${HOSTCFLAGS}\" ${MOPT}")
    autotools.make("prepare-all HOSTCFLAGS=\"${HOSTCFLAGS}\" ${MOPT}")

def install():
    pisitools.dodir("/usr/include/")

    shelltools.copytree("include/linux/", "%s/usr/include/linux/" % get.installDIR())
    shelltools.copytree("include/asm/", "%s/usr/include/asm/" % get.installDIR())
    shelltools.copytree("include/asm-generic/", "%s/usr/include/asm-generic/" % get.installDIR())
