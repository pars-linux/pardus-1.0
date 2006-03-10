#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde

def setup():
    kde.configure("--with-distribution=\"Pardus 1.0\" \
                   --enable-libfam \
                   --with-libart \
                   --with-libidn \
                   --with-utempter \
                   --with-alsa \
                   --with-arts \
                   --with-ssl \
                   --without-gssapi \
                   --with-tiff \
                   --with-jasper \
                   --without-openexr \
                   --with-cups \
                   --with-dnssd \
                   --with-aspell \
                   --with-acl \
                   --disable-fast-malloc")

def build():
    kde.make()
    kde.make("apidox")

def install():
    kde.install()
    kde.install("install-apidox")
