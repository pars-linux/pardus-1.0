#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr> 

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("keychain")
    pisitools.dodoc("ChangeLog", "keychain.pod", "README")
    pisitools.doman("keychain.1")
