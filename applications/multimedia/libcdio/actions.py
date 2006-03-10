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
# Please read the COPYING file.
# Timu EREN <selamtux@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-cddb")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % (get.installDIR()))
    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README", "THANKS")
