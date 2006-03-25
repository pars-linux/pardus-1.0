#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"

def setup():
    # Magic
    shelltools.system("agreed=1 sh j2sdk-1.4.2-03-linux-i586.bin")

    # go into work directory
    shelltools.cd("j2sdk1.4.2")
    shelltools.chmod("lib/unpack")

    PACKED_JARS=("lib/tools.jar", "jre/lib/rt.jar", "jre/lib/jsse.jar", \
               "jre/lib/charsets.jar", "jre/lib/ext/localedata.jar", "jre/lib/plugin.jar", \
               "jre/lib/javaws.jar")

    # Unpack all packed jars and remove pack files...
    for jar in PACKED_JARS:
        PACK_FILE = jar.replace("jar", "") + "pack"
        if shelltools.can_access_file(PACK_FILE):
            shelltools.system("lib/unpack %s %s" % (PACK_FILE, jar))
            shelltools.unlink(PACK_FILE)

    shelltools.unlink("lib/unpack")

def install():
    shelltools.cd("j2sdk1.4.2")
    pisitools.dodir("/opt/blackdown-jdk")

    INSTALL_DIRS = ("bin", "include", "jre", "lib", "man")

    for dir in INSTALL_DIRS:
        shelltools.copytree(dir, "%s/opt/blackdown-jdk/%s" % (get.installDIR(), dir))

    pisitools.dodoc("COPYRIGHT", "LICENSE", "README.html")

    # Install mozilla plugin
    pisitools.dodir("/usr/lib/nsbrowser/plugins")
    pisitools.dosym("/opt/blackdown-jdk/jre/plugin/i386/mozilla/libjavaplugin_oji.so", "/usr/lib/nsbrowser/plugins/javaplugin.so")
    
    pisitools.dosed("%s/opt/blackdown-jdk/jre/lib/font.properties" % get.installDIR(), "standard symbols l", "symbol")
