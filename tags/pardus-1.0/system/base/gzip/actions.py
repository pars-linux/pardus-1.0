#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--exec-prefix=/ --enable-nls")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%s/usr exec_prefix=%s/ mandir=%s/usr/share/man infodir=%s/usr/share/info" \
                         % (get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR()))

    # No need to waste space -- these guys should be links
    # gzcat is equivilant to zcat, but historically zcat
    # was a link to compress.
    pisitools.remove("/bin/gunzip")
    pisitools.remove("/bin/zcat")
    pisitools.remove("/bin/zcmp")
    pisitools.remove("/bin/zegrep")
    pisitools.remove("/bin/zfgrep")

    pisitools.dosym("gzip", "/bin/gunzip")
    pisitools.dosym("gzip", "/bin/gzcat")
    pisitools.dosym("gzip", "/bin/zcat")
    pisitools.dosym("zdiff", "/bin/zcmp")
    pisitools.dosym("zgrep", "/bin/zegrep")
    pisitools.dosym("zgrep", "/bin/zfgrep")

    pisitools.remove("/usr/share/man/man1/gunzip.1")
    pisitools.remove("/usr/share/man/man1/zcmp.1")
    pisitools.remove("/usr/share/man/man1/zcat.1")

    pisitools.dosym("gzip.1", "/usr/share/man/man1/gunzip.1")
    pisitools.dosym("zdiff.1", "/usr/share/man/man1/zcmp.1")
    pisitools.dosym("gzip.1", "/usr/share/man/man1/zcat.1")
    pisitools.dosym("gzip.1", "/usr/share/man/man1/gzcat.1")
       
    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO", "algorithm.doc", "gzip.doc")
