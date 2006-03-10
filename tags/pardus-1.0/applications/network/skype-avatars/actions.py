#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ali Erdinç Köroğlu <erdinc@erdinc.info>

from pisi.actionsapi import pisitools

WorkDir = "avatars"

def install():
    pisitools.dodir("/opt/skype")
    pisitools.dodir("/opt/skype/avatars")
    pisitools.insinto("/opt/skype/avatars", "*.jpg")
