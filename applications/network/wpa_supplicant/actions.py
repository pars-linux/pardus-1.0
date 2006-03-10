#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Furkan Duman <coderlord@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "wpa_supplicant-0.4.7"

def setup():
    config_setup()

def build():
    autotools.make()
    autotools.make("wpa_gui")

def install():
    pisitools.dosbin("wpa_supplicant")
    pisitools.dobin("wpa_cli")
    pisitools.dobin("wpa_passphrase")
    pisitools.dobin("wpa_gui/wpa_gui")
    pisitools.newdoc("wpa_supplicant.conf", "wpa_supplicant.conf.example")
    pisitools.dodoc("ChangeLog", "COPYING", "eap_testing.txt", "README", "todo.txt", "examples/*")
    pisitools.doman("doc/docbook/*.8")

def config_setup():
    CONFIGFILE = ".config"
  
    # Linux specific drivers
    shelltools.echo(CONFIGFILE, "CONFIG_WIRELESS_EXTENSION=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_HOSTAP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_WEXT=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_IPW=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_ATMEL=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_NDISWRAPPER=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_PRISM54=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_WIRED=y")
    # Pardus a bu suruculer eklendiginde acacagiz
    #shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_HERMES=n")
    #shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_MADWIFI=y")
    #shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_BROADCOM=y")
  
    # Basic authentication methods
    shelltools.echo(CONFIGFILE, "CONFIG_IEEE8021X_EAPOL=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_MD5=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_GTC=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_OTP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_PSK=y")
    shelltools.echo(CONFIGFILE, "CONFIG_PKCS12=y")
  
    # Smart card authentication
    #shelltools.echo(CONFIGFILE, "CONFIG_SMARTCARD=y")
    #shelltools.echo(CONFIGFILE, "CONFIG_EAP_SIM=y")
    #shelltools.echo(CONFIGFILE, "CONFIG_EAP_AKA=y")
    #shelltools.echo(CONFIGFILE, "CONFIG_PCSC=y")
  
    # Readline/history support for wpa_cli
    shelltools.echo(CONFIGFILE, "CONFIG_READLINE=y")
    shelltools.echo(CONFIGFILE, "CONFIG_CTRL_IFACE=y")
  
    # SSL authentication support
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_LEAP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_MSCHAPV2=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_PEAP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_TLS=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_TTLS=y")
