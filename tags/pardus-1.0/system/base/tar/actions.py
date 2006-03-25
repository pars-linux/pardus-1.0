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

def setup():
    autotools.configure("--enable-backup-scripts --bindir=/bin --libexecdir=/usr/sbin --enable-nls")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/sbin/rmt", "/etc/rmt")
    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "PORTS", "THANKS")

    pisitools.domove("/usr/sbin/backup", "/usr/sbin/", "backup-tar")
    pisitools.domove("/usr/sbin/restore", "/usr/sbin/", "restore-tar")
