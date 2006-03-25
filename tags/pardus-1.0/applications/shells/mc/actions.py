#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gürer Özen <gurer@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -I/usr/include/gssapi" % get.CFLAGS())
    autotools.configure("--with-screen=slang \
                         --with-gpm-mouse \
                         --with-included-gettext \
                         --with-vfs \
                         --with-gnu-ld \
                         --with-ext2undel \
                         --with-edit \
                         --enable-charset")

                         # --with-samba \
                         # --with-configdir=/etc/samba \
                         # --with-codepagedir=/var/lib/samba/codepages \
                         # --with-privatedir=/etc/samba/private \

def build():
    shelltools.export("CFLAGS", "%s -I/usr/include/gssapi" % get.CFLAGS())
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "AUTHORS", "MAINTAINERS", "FAQ", "INSTALL*", "NEWS", "README*")

    # install cons.saver setuid, to actually work
    shelltools.chmod("%s/usr/lib/mc/cons.saver" % get.installDIR(), 4755)

    # Do not mess with glibc files
    pisitools.remove("/usr/share/locale/locale.alias")

