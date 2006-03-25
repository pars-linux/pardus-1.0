#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # The date can be troublesome
    pisitools.dosed("configure", "`date`")

    # disable docs only disables docs generation (!)
    autotools.configure("--disable-docs \
                        --with-docdir=/usr/share/doc/%s \
                        --x-includes=/usr/X11R6/include \
                        --x-libraries=/usr/X11R6/lib \
                        --with-default-fonts=/usr/X11R6/lib/X11/fonts/Type1" % get.srcTAG())

    # this triggers sandbox, we do this ourselves
    pisitools.dosed("Makefile",  "fc-cache/fc-cache -f -v", "sleep 0")

def build():
    autotools.make()
    # remove Luxi TTF fonts from the list, the Type1 are much better
    pisitools.dosed("fonts.conf", "<dir>/usr/X11R6/lib/X11/fonts/TTF</dir>")
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/fonts", "fonts.conf")
    pisitools.insinto("/etc/fonts" "fonts.conf", "fonts.conf.new")

    pisitools.newman("fc-cache/fc-cache.man", "fc-cache.1")
    pisitools.newman("fc-list/fc-list.man", "fc-list.1")
    pisitools.newman("src/fontconfig.man", "fontconfig.3")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
