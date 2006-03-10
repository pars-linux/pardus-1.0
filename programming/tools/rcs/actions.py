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
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

InstDir = get.installDIR()
manDir = get.manDIR()


def setup():
    autotools.rawConfigure("--with-diffutils \
                            --prefix=/%s \
                            --host=%s \ " %
                            (get.defaultprefixDIR(), \
                             get.HOST()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%s/usr \
                          man1dir=%s/%s/man1 \
                          man3dir=%s/%s/man3 \
                          man5dir=%s/%s/man5" %
                          (InstDir,InstDir,manDir,InstDir,
                          manDir,InstDir,manDir))
    pisitools.dodoc("ChangeLog", "CREDITS", "NEWS", "README", "REFS")
