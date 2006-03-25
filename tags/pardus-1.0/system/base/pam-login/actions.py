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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "pam_login-3.14"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install("rootexecbindir=%s/bin" % get.installDIR())

    # We use the one from shadow
    pisitools.removeDir("/etc/pam.d")

    pisitools.domo("po/tr.po", "tr", "pam_login.mo")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
