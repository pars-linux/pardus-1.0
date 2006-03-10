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

def setup():
    autotools.configure("--libdir=/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % (get.installDIR()))

    # We do not distribute this
    pisitools.remove("/usr/bin/dlist_test")

    # Move static libs to /usr/lib - no reason to have then in /lib
    pisitools.dodir("/usr/lib")
    pisitools.domove("/lib/*.a", "/usr/lib/")
    pisitools.dosym("../../lib/libsysfs.la", "/usr/lib/libsysfs.la")
    # We need a linker script in /usr/lib, else all apps just links against
    # the static library .. bug #4411
    libtools.gen_usr_ldscript("libsysfs.so")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "TODO")
    pisitools.dodoc("docs/libsysfs.txt")
