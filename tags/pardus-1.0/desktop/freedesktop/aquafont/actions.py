#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.makedirs("%s/usr/share/fonts/aquafont/" % get.installDIR());
    shelltools.copy("aquafont.ttf","%s/usr/share/fonts/aquafont/aquafont.ttf" % get.installDIR());
    
