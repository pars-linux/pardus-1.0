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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "cracklib,2.7"

def setup():
    pisitools.dosed("util/create-cracklib-dict", "/usr/dict/words", "/usr/share/dict/words")

def build():
    shelltools.export("CC", get.CC())
    shelltools.export("AR", get.AR())
    shelltools.export("LD", get.LD())

    autotools.make("all")

def install():
    # following directories needed for install!
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/sbin")
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")
    
    autotools.rawInstall("DESTDIR=%s LIBDIR=/usr/lib/" % get.installDIR())
    
    # correct permissions on static lib
    shelltools.chmod("%s/usr/lib/libcrack.a" % get.installDIR(), 0644)

    # put libcrack.so.2.7 in /lib for cases where /usr isn't available yet
    pisitools.domove("/usr/lib/libcrack.so.2.7", "/lib/")

    # This link is needed and not created
    pisitools.dosym("libcrack.so.2.7", "/lib/libcrack.so.2")
    pisitools.dosym("libcrack.so.2.7", "/lib/libcrack.so")

    shelltools.move("cracklib/packer.h", get.installDIR() + "/usr/include")

    #fix the permissions on it as they may be wrong in some cases
    shelltools.chmod(get.installDIR() + "/usr/include/packer.h", 0644)
    
    libtools.preplib("/usr/lib")
    libtools.preplib("/lib")
    
    libtools.gen_usr_ldscript("libcrack.so")

    pisitools.dodoc("HISTORY", "MANIFEST", "POSTER", "README")
