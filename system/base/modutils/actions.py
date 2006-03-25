# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file `http://www.gnu.org/copyleft/gpl.txt'.
#
#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-strip \
                         --prefix=/ \
                         --enable-insmod-static \
                         --disable-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CREDITS", "ChangeLog", "NEWS", "README", "TODO")

    for f in ["depmod", "insmod", "insmod.static", "modinfo"]:
        pisitools.rename("/sbin/" + f, f + ".old")

    pisitools.remove("/sbin/kallsyms");        pisitools.dosym("insmod.old", "/sbin/kallsyms")
    pisitools.remove("/sbin/kallsyms.static"); pisitools.dosym("insmod.static.old", "/sbin/kallsyms.static")
    pisitools.remove("/sbin/ksyms");           pisitools.dosym("insmod.old", "/sbin/ksyms")
    pisitools.remove("/sbin/ksyms.static");    pisitools.dosym("insmod.static.old", "/sbin/ksyms.static")
    pisitools.remove("/sbin/lsmod");           pisitools.dosym("insmod.old", "/sbin/lsmod.old")
    pisitools.remove("/sbin/modprobe");        pisitools.dosym("insmod.old", "/sbin/modprobe.old")
    pisitools.remove("/sbin/rmmod");           pisitools.dosym("insmod.old", "/sbin/rmmod.old")

    manDir = "/usr/share/man/man8/"

    for m in ["lsmod", "modprobe", "rmmod", "depmod", "insmod"]:
        pisitools.rename(manDir + m + ".8", m + ".old.8")
