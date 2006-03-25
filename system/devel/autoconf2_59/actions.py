#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "autoconf-2.59"

def setup():
    autotools.configure("--program-suffix=\"-2.59\"")
    # We want to transform the binaries, not the manpages
    pisitools.dosed("man/Makefile", "^program_transform_name", "2.59")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "NEWS", "README", "TODO", "THANKS", "ChangeLog", "ChangeLog.0", "ChangeLog.1")

    # binutils installs this infopage
    pisitools.remove("/usr/share/info/standards.info")
