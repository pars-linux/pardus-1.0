#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    # 4 ÇOMAR (-lcomar)
    kde.make("-f admin/Makefile.common")

    # the java test is problematic (see kde bug 100729) and
    # useless. All that's needed for java applets to work is
    # to have the 'java' executable in PATH.
    kde.configure("--with-dpms \
                  --with-arts \
                  --without-ldap \
                  --with-cups \
                  --with-gl \
                  --with-ssl \
                  --with-samba \
                  --without-openexr \
                  --without-sensors \
                  --with-libusb \
                  --with-libraw1394 \
                  --with-hal \
                  --with-pam=yes \
                  --without-java")

def build():
    kde.make()

def install():
    kde.install()

    # kdm want extra interest
    shelltools.cd("kdm")
    kde.install("GENKDMCONF_FLAGS=\"--no-old --no-backup --no-in-notice\" install")

    pisitools.remove("%s/share/templates/.source/emptydir" % get.kdeDIR())

    #fix #730
    pisitools.remove("%s/share/autostart/klipper.desktop" % get.kdeDIR())
    pisitools.remove("%s/share/autostart/ktip.desktop" % get.kdeDIR())

    # we don't need kpersonalizer in Pardus
    pisitools.remove("%s/share/applications/kde/kpersonalizer.desktop" % get.kdeDIR())
    pisitools.remove("%s/bin/kpersonalizer" % get.kdeDIR())
    pisitools.removeDir("%s/share/apps/kpersonalizer" % get.kdeDIR())

    # remove kdeprintfax, it doesn't work (#1347)
    pisitools.removeDir("%s/share/apps/kdeprintfax" % get.kdeDIR())
    pisitools.remove("%s/share/applications/kde/kdeprintfax.desktop" % get.kdeDIR())
    pisitools.remove("%s/bin/kdeprintfax" % get.kdeDIR())
    
    # remove KDE's wallpapers, we've our own ;)
    pisitools.remove("%s/share/wallpapers/*" % get.kdeDIR())

    # Clean up settings menu
    pisitools.remove("/usr/kde/3.5/share/applnk/Settingsmenu/printmgr.desktop")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/kmenuedit.desktop")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/kappfinder.desktop")

