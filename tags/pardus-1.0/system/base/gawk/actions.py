#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--bindir=/bin --enable-nls")

def build():
    autotools.make()
    shelltools.cd(get.workDIR() + "/" + get.srcDIR() + "/filefuncs")
    autotools.make("AWKINCDIR=%s CC=%s" % (get.workDIR() + "/" + get.srcDIR(), get.CC()))
    shelltools.cd(get.workDIR() + "/" + get.srcDIR())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd(get.workDIR() + "/" + get.srcDIR() + "/filefuncs")
    autotools.rawInstall("DESTDIR=%s AWKINCDIR=%s LIBDIR=/lib" % (get.installDIR(), get.workDIR() + "/" + get.srcDIR()))
    shelltools.cd(get.workDIR() + "/" + get.srcDIR())

    pisitools.dodir("/usr/bin")

    binpath, d, ver = "", get.installDIR() + "/", get.srcVERSION()

    for i in ["gawk", "pgawk", "igawk"]:
        if i == "gawk":
            binpath = "/bin/"
        else:
            binpath = "/usr/bin/"

        if shelltools.can_access_file(d + "bin/" + i) and not shelltools.can_access_file(d + "bin/" + i + "-" + ver): 
            pisitools.domove("/bin/" + i, binpath, i + "-" + ver)
        elif shelltools.can_access_file(d + "bin/" + i + "-") and not shelltools.can_access_file(d + "bin/" + i + "-" + ver):
            pisitools.domove("/bin/" + i + "-", binpath, i + "-" + ver)
        elif binpath is "/usr/bin/"  and shelltools.can_access_file(d + "bin/" + i + "-" + ver):
            pisitools.domove("/bin/" + i + "-" + ver, binpath, i + "-" + ver)

        if shelltools.can_access_file(d + "bin/" + i):
            pisitools.remove("/bin/" + i)
            pisitools.dosym(i + "-" + ver, binpath + i)
        if binpath is "/usr/bin/":
            pisitools.dosym("/usr/bin/" + i + "-" + ver, "/bin/" + i)

    pisitools.dosym("igawk-" + ver, "/usr/bin/igawk")
    pisitools.dosym("/bin/gawk-" + ver, "/usr/bin/awk")
    pisitools.dosym("/bin/gawk-" + ver, "/usr/bin/gawk")

    pisitools.dodir("/usr/include/awk")

    for h in shelltools.ls(get.workDIR() + "/" + get.srcDIR() + "/*.h"):
        pisitools.insinto("/usr/include/awk/", h)

    if shelltools.can_access_file(d + "/usr/include/awk/acconfig.h"):
        pisitools.remove("/usr/include/awk/acconfig.h")

    pisitools.dosym("gawk.1", "/usr/share/man/man1/awk.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "FUTURES", "LIMITATIONS", "NEWS", "PROBLEMS", "POSIX.STD", "README")

    for f in shelltools.ls("README_d/"):
        pisitools.newdoc("README_d/%s" % f, "README_d/%s" % f)
    pisitools.newdoc("awklib/ChangeLog", "awklib/ChangeLog")
    pisitools.newdoc("pc/ChangeLog", "pc/ChangeLog")
    pisitools.newdoc("posix/ChangeLog", "posix/ChangeLog")
