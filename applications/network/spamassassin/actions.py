#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

WorkDir="Mail-SpamAssassin-3.1.0"

def setup():
    perlmodules.configure("/usr BUILD_SPAMC=\"yes\" ENABLE_SSL=\"yes\" CONTACT_ADDRESS=\"root@localhost\"")
                      
def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("README", "MANIFEST", "Changes")
