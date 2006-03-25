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

WorkDir="fftw-3.0.1"

def setup():
    shelltools.copytree("../fftw-3.0.1", "../fftw-3.0.1-double")
    
    shelltools.export("LDFLAGS","-L/usr/lib/gcc/i686-pc-linux-gnu/")
    autotools.configure("--enable-sse \
                        --enable-shared \
                        --enable-threads \
                        --enable-float")
                        
    shelltools.cd("../fftw-3.0.1-double")

    #the only difference here is no --enable-float
    autotools.configure("--enable-sse2 \
                        --enable-shared \
                        --enable-threads")

def build():
    autotools.make()
    shelltools.cd("../fftw-3.0.1-double")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../fftw-3.0.1-double")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        
    shelltools.cd("../fftw-3.0.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", \
                    "README", "TODO", "COPYRIGHT", "CONVENTIONS")

    pisitools.dohtml("doc/html")
