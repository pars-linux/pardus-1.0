#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="live"

def setup():
    shelltools.system("./genMakefiles linux")
    
def build():
    autotools.make()

def install():
    shelltools.makedirs("%s/usr/lib/live/BasicUsageEnvironment" % get.installDIR())
    shelltools.makedirs("%s/usr/lib/live/groupsock" % get.installDIR())
    shelltools.makedirs("%s/usr/lib/live/liveMedia" % get.installDIR())
    shelltools.makedirs("%s/usr/lib/live/UsageEnvironment" % get.installDIR())
    
    shelltools.copy("BasicUsageEnvironment/include", "%s/usr/lib/live/BasicUsageEnvironment/include" % get.installDIR())
    shelltools.copy("BasicUsageEnvironment/*.a", "%s/usr/lib/live/BasicUsageEnvironment/" % get.installDIR())

    shelltools.copy("groupsock/include", "%s/usr/lib/live/groupsock/include" % get.installDIR())
    shelltools.copy("groupsock/*.a", "%s/usr/lib/live/groupsock/" % get.installDIR())

    shelltools.copy("liveMedia/include", "%s/usr/lib/live/liveMedia/include" % get.installDIR())
    shelltools.copy("liveMedia/*.a", "%s/usr/lib/live/liveMedia/" % get.installDIR())

    shelltools.copy("UsageEnvironment/include", "%s/usr/lib/live/UsageEnvironment/include" % get.installDIR())
    shelltools.copy("UsageEnvironment/*.a", "%s/usr/lib/live/UsageEnvironment/" % get.installDIR())

