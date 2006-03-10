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

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure("--with-ssl \
                         --with-nsl \
                         --enable-LFS \
                         --sysconfdir=/etc/wget \
                         --enable-ipv6 \
                         --enable-nls \
                         --prefix=/%s \
                         --host=%s \
                         --mandir=/%s \
                         --infodir=/%s \
                         --datadir=/%s \
                         --localstatedir=/%s \
                        " % (get.defaultprefixDIR(), \
                         get.HOST(), get.manDIR(), \
                         get.infoDIR(), get.dataDIR(), \
                         get.localstateDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "MACHINES", "MAILING-LIST", "NEWS", "README", "TODO", "doc/sample.wgetrc")
