#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools

def setup():
    autotools.aclocal()
    autotools.autoconf()
    libtools.libtoolize("--copy --force")
    autotools.configure()

def configure():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "NEWS", "TODO", "README*", "doc/interface*")
