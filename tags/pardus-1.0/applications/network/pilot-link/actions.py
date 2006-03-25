#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--includedir=/usr/include/libpisock \
                         --with-java=no \
                         --with-perl=yes \
                         --with-python=yes \
                         --with-libpng=/usr \
                         --with-readline=yes")

def build():
    autotools.make()
    #FIXME
    #for [source]/bindings/Perl,
    #perl-module_src_prep
    #perl-module_src_compile


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "doc/README*", "doc/TODO", "NEWS", "AUTHORS")
    #FIXME
    #for [source]/bindings/Perl,
    #perl-module_src_install
