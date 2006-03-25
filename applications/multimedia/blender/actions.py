# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file `http://www.gnu.org/copyleft/gpl.txt'.
#
#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "blender"

def setup():
    shelltools.cd("release/plugins") 
    shelltools.chmod("bmake", 0755)
    pisitools.removeDir("include")
    shelltools.cd("../..")
    shelltools.copytree("%s/blender/source/blender/blenpluginapi" % get.workDIR(), "./include")
    for dir in ["extern", "intern", "source"]:
        pisitools.dodir("%s/build/linux2/%s" % (get.workDIR(), dir))


def build():
    # Build game engine..
    pisitools.dosed("config.opts", "BUILD_GAMEENGINE.*$", "BUILD_GAMEENGINE = 'true'")

    pisitools.dosed("SConstruct", "-02", "%s" % get.CFLAGS())

    scons.make()
    shelltools.cd("release/plugins")
    autotools.make()

def install():
    pisitools.dobin("blender")
    pisitools.dobin("blenderplayer")

    pisitools.doexe("release/plugsins/texture/*.so", "/usr/lib/blender/textures")
    pisitools.doexe("release/plugsins/sequence/*.so", "/usr/lib/blender/sequences")

    for file in ["bpydata", "plugins", "scripts"]:
        pisitools.insinto("/usr/lib/blender/", "release/%s" % file) 
   
    pisitools.dodoc("COPYING", "INSTALL", "README", "release_237.txt") 

