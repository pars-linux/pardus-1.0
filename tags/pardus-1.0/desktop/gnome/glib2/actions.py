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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "glib-2.8.3"

def setup():
    autotools.configure("--with-threads=posix --enable-static --disable-gtk-doc")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # Consider invalid UTF-8 filenames as locale-specific.
    # WARN: we should probably move to suggesting G_FILENAME_ENC
    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/50glib2" % get.installDIR(),  "G_BROKEN_FILENAMES=1")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "README*", "INSTALL", "NEWS*")
