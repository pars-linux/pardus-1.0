#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls")

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

def install():
    autotools.install()

    pisitools.dobin("sed/sed", "/bin")

    pisitools.remove("/usr/bin/sed")

    pisitools.dosym("/bin/sed", "/usr/bin/sed")

    pisitools.dodoc("NEWS", "README*", "THANKS", "AUTHORS", "BUGS", "ChangeLog")

    pisitools.newdoc("doc/dos2unix", "example/dos2unix")
    pisitools.newdoc("doc/unix2dos", "example/unix2dos")
