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
from pisi.actionsapi import get

WorkDir = "ImageMagick-6.2.5"

def setup():
    autotools.configure("--with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --enable-shared \
                         --enable-lzw \
                         --without-hdf \
                         --with-threads \
                         --with-bzlib \
                         --with-modules \
                         --with-zlib \
                         --with-x \
                         --with-wmf \
                         --without-fpx \
                         --with-perl \
                         --without-jbig \
                         --with-tiff \
                         --with-lcms \
                         --with-xml \
                         --with-jp2 \
                         --with-jpeg \
                         --with-mpeg2 \
                         --with-gslib \
                         --with-dot \
                         --with-ttf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/libltdl*")
    pisitools.remove("/usr/lib/perl5/*/*/perllocal.pod")

#    pisitools.dosed("/usr/bin/Magick-config", "-I/usr/include ")
#    pisitools.dosed("usr/bin/Magick++-config", "-I/usr/include ")
