#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "portmap_5b"

def build():
    autotools.make('CC="%s" \
                    O="-mcpu=i686 -O2 -pipe -fomit-frame-pointer -DHOSTS_ACCESS -DHOSTS_ACCESS" \
                    WRAP_LIB="-lwrap"' % get.CC())

def install():
    pisitools.dosbin("portmap", "/sbin")
    pisitools.dosbin("pmap_dump")
    pisitools.dosbin("pmap_set")

    pisitools.doman("portmap.8", "pmap_dump.8", "pmap_set.8")
    pisitools.dodoc("BLURB", "CHANGES", "README")
