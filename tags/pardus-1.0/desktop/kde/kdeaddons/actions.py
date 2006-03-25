#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import kde

def setup():
    kde.configure("--with-sdl \
                  --without-xmms \
                  --with-berkeley-db \
                  --with-db-lib=db_cxx-4.2 \
                  --with-extra-includes=/usr/include/db4.2")

def build():
    kde.make()

def install():
    kde.install()
