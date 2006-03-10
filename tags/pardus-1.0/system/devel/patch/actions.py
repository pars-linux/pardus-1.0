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
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("CFLAGS", get.CFLAGS() + " -DLINUX -D_XOPEN_SOURCE=500")
    shelltools.export("ac_cv_sys_long_file_names", "yes")
    autotools.rawConfigure("%s --prefix=/usr --mandir=/usr/share/man" % get.HOST())

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
