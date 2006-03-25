#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-gpl \
                            --enable-pthreads \
                            --enable-pp \
                            --enable-a52 \
                            --enable-x264 \
                            --enable-xvid \
                            --enable-faad \
                            --enable-faac \
                            --enable-vorbis \
                            --enable-mp3lame \
                            --enable-libogg \
                            --enable-theora \
                            --enable-dts \
                            --enable-amr_nb \
                            --enable-amr_wb \
                            --enable-dc1394 \
                            --enable-shared \
                            --enable-shared-pp")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
   
    pisitools.dodoc("Changelog", "README")
    pisitools.doman("man.1", "doc/ff*.1")
    pisitools.dohtml("doc/faq.html", "doc/ffmpeg-doc.html", "doc/ffplay-doc.html", "doc/ffserver-doc.html", "doc/hooks.html") 
    
    # Copy ffserver.conf
    pisitools.insinto("/etc", "doc/ffserver.conf")

