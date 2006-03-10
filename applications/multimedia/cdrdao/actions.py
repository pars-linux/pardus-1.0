#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("scsilib/include/xmconfig.h", "HAVE_SCANSTACK", "NO_FRIGGING_SCANSTACK")
    pisitools.dosed("scsilib/include/mconfig.h", "HAVE_SCANSTACK", "NO_FRIGGING_SCANSTACK")
        
    autotools.configure("--build=\"i686-pc-linux-gnu\" --host=\"i686-pc-linux-gnu\" --prefix=/usr --enable-debug")
                        
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "CREDITS", "ChangeLog", "NEWS", "README*")

