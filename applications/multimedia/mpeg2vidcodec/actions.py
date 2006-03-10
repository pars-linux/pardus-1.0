#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Timu EREN <selamtux@gmail.com>
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mpeg2"

def setup():
     pisitools.dosed("Makefile", "-O2", get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("src/mpeg2dec/mpeg2decode")
    pisitools.dobin("src/mpeg2enc/mpeg2encode")

    pisitools.dodoc("README", "doc/*")
