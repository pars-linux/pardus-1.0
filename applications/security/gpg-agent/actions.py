#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gnupg-1.9.9"

def setup():
    autotools.configure("--enable-agent-only \
                         --disable-scdaemon \
                         --disable-gpgsm \
                         --enable-symcryptrun \
                         --enable-nls \
                         --without-capabilities")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.chmod("%s/usr/bin/gpg-agent" % get.installDIR(), 04711)
