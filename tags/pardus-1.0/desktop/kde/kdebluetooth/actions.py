#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    # Change defaults to match our bluez-utils setup
    pisitools.dosed("kdebluetooth/kbluetoothd/kcm_btpaired/pairedtab.cpp", "/etc/init.d/bluez-utils", "/etc/init.d/bluetooth")

    kde.configure()
    
def build():
    kde.make()
    
def install():
    kde.install()
