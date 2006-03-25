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
from pisi.actionsapi import get

WorkDir = "rc-scripts-0.4.1"

def build():
    autotools.make("-C src CC=\"%s\" LD=\"%s %s\" CFLAGS=\"%s\"" % (get.CC(), get.CC(), get.LDFLAGS(), get.CFLAGS()))
        
def install():
    # Setup files in /etc
    pisitools.dodir("/etc")
    shelltools.move("etc/", "%s/etc" % get.installDIR())

    shelltools.chmod("%s/etc/shadow" % get.installDIR(), 0600)

    # Install some files to /usr/share/baselayout instead of /etc to keep from overwriting the user's settings,
    for file in ("passwd", "shadow", "group", "fstab", "hosts"):
        pisitools.domove("/etc/%s" % file, "/usr/share/baselayout")
    
    # Install init scripts
    shelltools.move("init.d/", "%s/etc/init.d" % get.installDIR())
    shelltools.move("rc-lists", "%s/usr/share/baselayout/rc-lists" % get.installDIR())

    # sysvinit is its own package again, and provides the inittab itself
    pisitools.remove("/etc/inittab")

    # Setup files related to /dev
    pisitools.dosbin("sbin/MAKEDEV", "/sbin")
    pisitools.dosym("../../sbin/MAKEDEV", "/usr/sbin/MAKEDEV")
    pisitools.dosym("../sbin/MAKEDEV", "/dev/MAKEDEV")

    # Setup files in /bin
    pisitools.dobin("bin/rc-status", "/bin")
    pisitools.dobin("bin/bashlogin", "/bin")
    pisitools.dobin("bin/xlogin", "/bin")
   
    # Setup files in /sbin 
    pisitools.dosbin("sbin/rc", "/sbin")
    pisitools.dosbin("sbin/rc-update", "/sbin")

    # Need this in /sbin, as it could be run before /usr is mounted.
    pisitools.dosbin("sbin/modules-update", "/sbin")

    # Compat symlinks until I can get things synced.
    pisitools.dosym("modules-update", "/sbin/update-modules")
    pisitools.dosym("../../sbin/modules-update", "/usr/sbin/update-modules")

    # These moved from /etc/init.d/ to /sbin to help newb systems from breaking
    pisitools.dosbin("sbin/runscript.sh", "/sbin")
    pisitools.dosbin("sbin/functions.sh", "/sbin")
    pisitools.dosbin("sbin/livecd-functions.sh", "/sbin")

    # Compat symlinks between /etc/init.d and /sbin (some stuff have hardcoded paths)
    pisitools.dosym("../../sbin/depscan.sh", "/etc/init.d/depscan.sh")
    pisitools.dosym("../../sbin/runscript.sh", "/etc/init.d/runscript.sh")
    pisitools.dosym("../../sbin/functions.sh", "/etc/init.d/functions.sh")
  
    # Setup files in /lib/rcscript
    pisitools.doexe("sbin/rc-services.sh", "/lib/rcscripts/sh")
    pisitools.doexe("sbin/rc-daemon.sh", "/lib/rcscripts/sh")
    pisitools.doexe("sbin/rc-help.sh", "/lib/rcscripts/sh")

    # This is for new depscan.sh and env-update.sh written in awk
    pisitools.dosbin("sbin/depscan.sh", "/sbin")
    pisitools.dosbin("sbin/env-update.sh", "/sbin")
    
    pisitools.insinto("/lib/rcscripts/awk", "src/awk/cachedepends.awk")
    pisitools.insinto("/lib/rcscripts/awk", "src/awk/functions.awk")
    pisitools.insinto("/lib/rcscripts/awk", "src/awk/gendepends.awk")
    pisitools.insinto("/lib/rcscripts/awk", "src/awk/genenviron.awk")

    # Install baselayout documentation
    pisitools.doman("man/*.*")
    pisitools.dodoc("ChangeLog")

    # i18n support for Turkish
    pisitools.insinto("/etc", "i18n/init.tr")

    # Install baselayout utilities
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

    # Create needed directories !!!
    create_directories()

def kdir(directory, parameters = ""):
    """ local function to create needed directories """
    shelltools.system("install -d %s %s/%s" % (parameters, get.installDIR(), directory))

def create_directories():
    kdir("/boot")
    kdir("/initrd")
    kdir("/dev")
    kdir("/dev/pts")
    kdir("/dev/shm")
    kdir("/etc/conf.d")
    kdir("/etc/cron.daily")
    kdir("/etc/cron.hourly")
    kdir("/etc/cron.monthly")
    kdir("/etc/cron.weekly")
    kdir("/etc/env.d")
    kdir("/etc/init.d")          
    kdir("/etc/modules.autoload.d")
    kdir("/etc/modules.d")
    kdir("/etc/opt")
    kdir("/home")
    kdir("/lib")
    kdir("/lib/dev-state")
    kdir("/lib/udev-state")
    kdir("/lib/rcscripts/awk")
    kdir("/lib/rcscripts/sh")
    kdir("/mnt")
    kdir("/mnt/floppy", "-m 0700")
    kdir("/opt")
    kdir("/var/lock", "-o root -g uucp -m0755")
    kdir("/proc")
    kdir("/sbin")
    kdir("/sys")
    kdir("/usr")
    kdir("/usr/bin")
    kdir("/usr/include")
    kdir("/usr/include/asm")
    kdir("/usr/include/linux")
    kdir("/usr/lib")
    kdir("/usr/local/bin")
    kdir("/usr/local/games")
    kdir("/usr/local/lib")
    kdir("/usr/local/sbin")
    kdir("/usr/local/share")
    kdir("/usr/local/share/doc")
    kdir("/usr/local/share/man")
    kdir("/usr/local/src")
    kdir("/usr/sbin")
    kdir("/usr/share/doc")
    kdir("/usr/share/info")
    kdir("/usr/share/man")
    kdir("/usr/share/misc")
    kdir("/usr/src")
    kdir("/tmp", "-m 01777")
    kdir("/var")
    kdir("/var/lib/misc")
    kdir("/var/lock/subsys")
    kdir("/var/log/news")
    kdir("/var/run")
    kdir("/var/spool")
    kdir("/var/state")
    kdir("/var/tmp", "-m 01777")

    # FHS compatibility symlinks stuff
    pisitools.dosym("/var/tmp", "/usr/tmp")
    pisitools.dosym("share/man", "/usr/local/man")
