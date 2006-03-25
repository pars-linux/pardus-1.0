#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "gcc-3.4.5"

# Global Path Variables
PREFIX = "/usr"
BINPATH = "/usr/%s/gcc-bin/3.4.5" % get.HOST()
LIBPATH = "/usr/lib/gcc/%s/3.4.5" % get.HOST()
INCDIR = "/usr/lib/gcc/%s/3.4.5/include" % get.HOST()
DATAPATH = "/usr/share/gcc-data/%s/3.4.5" % get.HOST()
MANPATH = "/usr/share/gcc-data/%s/3.4.5/man" % get.HOST()
INFOPATH = "/usr/share/gcc-data/%s/3.4.5/info" % get.HOST()
STDCXX_INCDIR = "/usr/lib/gcc/%s/3.4.5/include/g++-v3" % get.HOST()

def setup():
    pisitools.dosed("gcc/config.in", "HAVE_LD_AS_NEEDED", "USE_LD_AS_NEEDED")
    
    # Branding :P
    pisitools.dosed("gcc/version.c", "<URL:http://gcc.gnu.org/bugs.html>" , "<URL:http://bugs.pardus.org.tr>")
    
    libtools.gnuconfig_update()

    shelltools.export("GCC_LANG", "c,c++,objc,f77")

    # Gcc don't like mcpu flag while bootstrapping itself
    shelltools.export("CFLAGS", "-march=i686 -O2 -pipe -fomit-frame-pointer")
    shelltools.export("CXXFLAGS", "-march=i686 -O2 -pipe -fomit-frame-pointer")

    conf ="--enable-version-specific-runtime-libs \
           --prefix=%s \
           --bindir=%s \
           --includedir=%s \
           --datadir=%s \
           --mandir=%s \
           --infodir=%s \
           --with-gxx-include-dir=%s \
           --host=%s \
           --build=%s \
           --disable-altivec \
           --disable-nls \
           --without-included-gettext \
           --with-system-zlib \
           --disable-checking \
           --disable-werror \
           --disable-libunwind-exceptions \
           --disable-multilib \
           --enable-languages=c,c++,objc,f77 \
           --enable-shared \
           --enable-threads=posix \
           --enable-__cxa_atexit \
           --enable-clocale=gnu" % (PREFIX, BINPATH, INCDIR, DATAPATH, MANPATH, INFOPATH, STDCXX_INCDIR, get.HOST(), get.HOST())

    shelltools.makedirs("%s/build" % get.workDIR())
    shelltools.cd("%s/build" % get.workDIR())
    shelltools.system("%s/%s/configure %s" % (get.workDIR(), WorkDir, conf))

def build():
    # Gcc 3.4 don't like mcpu flag while bootstrapping itself
    shelltools.export("CFLAGS", "-march=i686 -O2 -pipe -fomit-frame-pointer")
    shelltools.export("CXXFLAGS", "-march=i686 -O2 -pipe -fomit-frame-pointer")
    
    shelltools.touch("gcc/c-gperf.h")

    shelltools.cd("%s/build" % get.workDIR())
    autotools.make("LDFLAGS=\"%s\" STAGE1_CFLAGS=\"-O\" LIBPATH=\"%s\" BOOT_CFLAGS=\" -march=i686 -O2 -pipe\" profiledbootstrap" % (get.LDFLAGS(), LIBPATH))

def install():
    shelltools.cd("%s/build" % get.workDIR())
    
    conf = "DESTDIR=%s \
            prefix=%s \
            bindir=%s \
            includedir=%s/include \
            datadir=%s \
            mandir=%s/man \
            infodir=%s/info \
            LIBPATH=%s \
            ${GCC_INSTALL_TARGET}" % (get.installDIR(), PREFIX, BINPATH, LIBPATH, DATAPATH, DATAPATH, DATAPATH, LIBPATH)

    autotools.make(conf)

    for file in shelltools.ls("%s/build/gcc/include/*" % get.workDIR()):
        if shelltools.isLink(file):
            shelltools.unlink(file)

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # This one comes with binutils
    pisitools.remove("/usr/lib/libiberty.a")

    for file in ("%s/libstdc++.la" % LIBPATH, "%s/libsupc++.la" % LIBPATH):
        pisitools.dosed("%s%s" % (get.installDIR(),file), "^libdir.*", "libdir=%s" % shelltools.baseName(file))

    # Move Java headers to compiler-specific dir
    pisitools.domove("/usr/lib/security", LIBPATH)
    pisitools.domove("/usr/lib/lib*", LIBPATH)

    # Move <cxxabi.h> to compiler-specific directories
    pisitools.move("%s/cxxabi.h" % STDCXX_INCDIR, "%s/include/" % LIBPATH)

    # These should be symlinks
    for binary in ("gcc", "g++", "c++"):
        pisitools.remove("%s/%s" % (BINPATH, binary))
        pisitools.dosym("%s-%s" % (get.HOST(), binary), "%s/%s" % (BINPATH, binary))
        # /usr/bin symlinks
        pisitools.dosym("%s/%s" % (BINPATH, binary), "/usr/bin/%s" % binary)

    # /usr/bin symlinks
    pisitools.dosym("%s/gcc" % BINPATH, "/usr/bin/cc")
    pisitools.dosym("%s/cpp" % BINPATH, "/usr/bin/cpp")
    
    # i686-... symlinks 
    pisitools.dosym("%s/gcc" % BINPATH, "/usr/bin/%s-gcc" % get.HOST())
    pisitools.dosym("%s/g++" % BINPATH, "/usr/bin/%s-g++" % get.HOST())
    pisitools.dosym("%s/c++" % BINPATH, "/usr/bin/%s-c++" % get.HOST())
    pisitools.dosym("%s/g77" % BINPATH, "/usr/bin/%s-g77" % get.HOST())

    # For some reason, g77 and gcjh gets made instead of ${CTARGET}-g77... this makes it safe
    pisitools.domove("%s/g77" % BINPATH, "%s/" % BINPATH ,"%s-g77" %  get.HOST())
    pisitools.dosym("%s-g77" % get.HOST(), "%s/g77" % BINPATH)

    # Fix libstdc++ path
    pisitools.dosed("%s/usr/lib/gcc/i686-pc-linux-gnu/3.4.5/libstdc++.la" % get.installDIR(), 
                    "libdir=libstdc\\+\\+.la", "libdir='/usr/lib/gcc/i686-pc-linux-gnu/3.4.5'")
