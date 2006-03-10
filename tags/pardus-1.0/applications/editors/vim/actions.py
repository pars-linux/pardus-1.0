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

WorkDir = "vim64"

def setup():
    pisitools.dosed("runtime/tools/mve.awk", "#!/usr/bin/nawk -f", "#!/usr/bin/awk -f")
    
    shelltools.echo("src/feature.h", "#define SYS_VIMRC_FILE \"/etc/vim/vimrc\"")

    pisitools.dosed("runtime/doc/syntax.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/tagsrch.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/usr_29.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/menu.vim", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("src/configure.in", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")

    pisitools.dosed("src/configure.in", " libc\.h ", " ")
    pisitools.dosed("src/Makefile", " auto.config.mk:", ":")

    pisitools.remove("src/auto/configure")

    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.make("-C src autoconf")

    autotools.configure("--with-features=huge \
                         --enable-multibyte \
                         --enable-perlinterp \
                         --enable-pythoninterp \
                         --enable-gui=no \
                         --with-tlib=ncurses \
                         --disable-acl \
                         --disable-selinux \
                         --without-x")
def build():
    autotools.make("-C src auto/osdef.h objects")

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/etc/vim")
    pisitools.dodir("/usr/share")
    pisitools.dodir("/usr/share/man")
    pisitools.dodir("/usr/share/vim")
    pisitools.dodir("/usr/share/vim/vim64")
    pisitools.dodir("/usr/share/vim/vim64/plugin")

    shelltools.cd("src/")
    autotools.rawInstall("installruntime \
                          installhelplinks \
                          installmacros \
                          installtutor \
                          installtools \
                          install-languages \
                          install-icons \
                          DESTDIR=%s \
                          BINDIR=/usr/bin \
                          MANDIR=/usr/share/man \
                          DATADIR=/usr/share" % get.installDIR())
    shelltools.cd("../")

    pisitools.dobin("src/vim")
    pisitools.dosym("vim", "/usr/bin/vi")
