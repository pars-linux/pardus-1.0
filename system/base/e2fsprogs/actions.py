#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    # Fix permission problems
    shelltools.chmod("/po/*.po", 0777)
    shelltools.chmod("config*", 0777)
    
    shelltools.export("LDCONFIG", "/bin/true")
    autotools.configure("--enable-dynamic-e2fsck --enable-elf-shlibs --enable-nls")
    
def build():
     # Parallel make sometimes fails
    autotools.make("-j1")

def install():
    #evil e2fsprogs makefile -- I'll get you!
    autotools.rawInstall("DESTDIR=%s libdir=/zapme" % get.installDIR())
    pisitools.removeDir("/zapme")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-libs")

    pisitools.dodoc("ChangeLog", "README", "RELEASE-NOTES", "SHLIBS", "e2fsck/ChangeLog", "e2fsck/CHANGES")

    pisitools.domove("/usr/lib/", "/lib")
    pisitools.domove("/lib/*.a", "/usr/lib")

    for file in shelltools.ls("%s/usr/lib/*.a" % get.installDIR()):
        destination = file.replace(get.installDIR(), "")
        destination = destination.split("/")[3]
        # create new ldscript
        libtools.gen_usr_ldscript(destination.replace(".a", ".so"))

    # normalize evil symlinks
    for link in shelltools.ls("%s/lib/*" % get.installDIR()):
        if shelltools.isLink(link) and not shelltools.can_access_file(shelltools.realPath(link)):
            source = shelltools.baseName(shelltools.realPath(link))
            link = link.replace(get.installDIR(), "")
            # remove old link
            pisitools.remove(link)
            # create new link
            pisitools.dosym(source, link)
           
    pisitools.domove("/usr/sbin/", "/sbin")

    pisitools.domove("/usr/bin/lsattr", "/bin")
    pisitools.domove("/usr/bin/chattr", "/bin")
    pisitools.domove("/usr/bin/uuidgen", "/bin")

    pisitools.domove("/sbin/mklost+found",  "/usr/sbin")

    # time to convert hard links/duplicates to symbolic links
    pisitools.remove("/sbin/fsck.ext2")
    pisitools.dosym("/sbin/e2fsck", "/sbin/fsck.ext2")
    pisitools.remove("/sbin/fsck.ext3")
    pisitools.dosym("/sbin/e2fsck", "/sbin/fsck.ext3")

    pisitools.remove("/sbin/mkfs.ext2")
    pisitools.dosym("/sbin/mke2fs", "/sbin/mkfs.ext2")
    pisitools.remove("/sbin/mkfs.ext3")
    pisitools.dosym("/sbin/mke2fs", "/sbin/mkfs.ext3")

    # copy compile_et & mk_cmds
    shelltools.copy("%s/lib/et/compile_et" % get.curDIR(), "%s/bin/" % get.installDIR())
    shelltools.copy("%s/lib/ss/mk_cmds" % get.curDIR(), "%s/bin/" % get.installDIR())
    
    # Symlink com_err.h
    pisitools.dosym("/usr/include/et/com_err.h","/usr/include/com_err.h")

