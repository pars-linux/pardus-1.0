#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Furkan Duman <coderlord@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-ipv6")

def build():
    autotools.make()
    autotools.make("shared")

def install():
    autotools.install()
    pisitools.dolib_so("libpcap.so.0.9.4")
    pisitools.dosym("libpcap.so.0.9.4", "/usr/lib/libpcap.so")
    pisitools.dodoc("CHANGES", "CREDITS", "FILES", "README", "README.linux", "TODO", "VERSION", "/doc/pcap.txt")
