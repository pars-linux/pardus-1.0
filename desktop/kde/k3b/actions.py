#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import kde
from pisi.actionsapi import get

def setup():
    kde.configure("--enable-libsuffix= \
                   --with-external-libsamplerate \
                   --without-resmgr \
                   --with-musicbrainz \
                   --with-hal \
                   --with-lame \
                   --with-flac \
                   --with-oggvorbis \
                   --with-libmad \
                   --without-k3bsetup")

def build():
    kde.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FAQ", "INSTALL", "KNOWNBUGS", "PERMISSIONS", "README", "TODO")

    pisitools.removeDir("/usr/share/applnk/")
