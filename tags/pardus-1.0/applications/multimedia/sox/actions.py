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

def setup():
    #   SoX currently targets the ALSA kernel API and not alsa-lib. This is a problem because the interface changes.
    autotools.configure("--enable-ogg-vorbis \
                        --enable-mad \
                        --enable-lame \
                        --enable-oss-dsp \
                        --disable-alsa-dsp \
                        --enable-fast-ulaw \
                        --enable-fast-alaw")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("Changelog", "README", "TODO", "*.txt")
