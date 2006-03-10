#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr")

def build():
    autotools.make("all")
    autotools.make("rdf")

def install():
    pisitools.dobin("nasm")
    pisitools.dobin("ndisasm")
    pisitools.dobin("rdoff/ldrdf")
    pisitools.dobin("rdoff/rdf2bin")
    pisitools.dobin("rdoff/rdf2ihx")
    pisitools.dobin("rdoff/rdfdump")
    pisitools.dobin("rdoff/rdflib")
    pisitools.dobin("rdoff/rdx")

    pisitools.dosym("/usr/bin/rdf2bin", "/usr/bin/rdf2com")
    
    pisitools.doman("nasm.1", "ndisasm.1")
    
    pisitools.dodoc("AUTHORS", "CHANGES", "ChangeLog", "INSTALL", "README", "TODO", "doc/nasmdoc.*")
    
    pisitools.doinfo("doc/info/")
