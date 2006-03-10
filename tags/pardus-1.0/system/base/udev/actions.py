#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def generateStatic():
    autotools.make("clean")

    pisitools.dosed("Makefile", "USE_KLIBC = false", "USE_KLIBC = true")
    pisitools.dosed("Makefile", "USE_STATIC = false", "USE_KLIBC = true")

    autotools.make()

    pisitools.insinto("/sbin", "udev", "udev.static")

def setup():
    pisitools.dosed("Makefile", "$(OPTIMIZATION)")

def build():
    extras="extras/scsi_id extras/volume_id extras/ata_id extras/run_directory extras/usb_id extras/floppy extras/cdrom_id extras/firmware"
    autotools.make("EXTRAS=\"%s\" udevdir=\"/dev/\"" % extras)

def install():
    pisitools.dobin("udevinfo", "/bin")
    pisitools.dobin("udevtest", "/bin")
    pisitools.dobin("udevmonitor", "/bin")

    pisitools.dosbin("udev", "/sbin")
    pisitools.dosbin("udevd", "/sbin")
    pisitools.dosbin("udevsend", "/sbin")
    pisitools.dosbin("udevstart", "/sbin")
    pisitools.dosbin("udeveventrecorder", "/sbin")
    pisitools.dosbin("udevcontrol", "/sbin")

    pisitools.dosbin("extras/run_directory/udev_run_devd", "/sbin")
    pisitools.dosbin("extras/run_directory/udev_run_hotplugd", "/sbin")
    pisitools.dosbin("extras/ata_id/ata_id", "/sbin")
    pisitools.dosbin("extras/volume_id/vol_id", "/sbin")
    pisitools.dosbin("extras/scsi_id/scsi_id", "/sbin")
    pisitools.dosbin("extras/usb_id/usb_id", "/sbin")
    pisitools.dosbin("extras/cdrom_id/cdrom_id", "/sbin")
    pisitools.dosbin("extras/path_id", "/sbin")
    pisitools.dosbin("extras/floppy/create_floppy_devices", "/sbin")
    pisitools.dosbin("extras/firmware/firmware_helper" "/sbin")

    pisitools.doexe("extras/ide-devfs.sh", "/etc/udev/scripts/")
    pisitools.doexe("extras/raid-devfs.sh", "/etc/udev/scripts/")
    pisitools.doexe("extras/scsi-devfs.sh", "/etc/udev/scripts/")
    pisitools.doexe("extras/dvb.sh", "/etc/udev/scripts/")

    pisitools.insinto("/etc/udev/rules.d/", "etc/udev/gentoo/udev.rules", "50-udev.rules")

    # scsi_id configuration
    pisitools.insinto("/etc", "extras/scsi_id/scsi_id.config")

    # set up symlinks in /etc/hotplug.d/default
    pisitools.dodir("/etc/hotplug.d/default")
    pisitools.dosym("../../../sbin/udevsend", "/etc/hotplug.d/default/10-udev.hotplug")

    # set up the /etc/dev.d directory tree
    pisitools.dodir("/etc/dev.d/default")
    pisitools.dodir("/etc/dev.d/net")
    pisitools.doexe("extras/run_directory/dev.d/net/hotplug.dev", "/etc/dev.d/net")

    pisitools.doman("*.8")
    pisitools.doman("extras/ata_id/ata_id.8")
    pisitools.doman("extras/edd_id/edd_id.8")
    pisitools.doman("extras/scsi_id/scsi_id.8")
    pisitools.doman("extras/volume_id/vol_id.8")
    pisitools.doman("extras/dasd_id/dasd_id.8")
    pisitools.doman("extras/cdrom_id/cdrom_id.8")

    pisitools.dodoc("COPYING", "ChangeLog", "FAQ", "HOWTO-udev_for_dev", "README", "TODO", "RELEASE-NOTES")
    pisitools.dodoc("docs/overview", "docs/udev_vs_devfs")
    pisitools.dodoc("docs/writing_udev_rules/*")
    pisitools.newdoc("extras/volume_id/README", "README_volume_id")

    # Generate static one for initrd
    generateStatic()
