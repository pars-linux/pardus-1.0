#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE", "atlantik kastreoids katomic kbackgammon kblackbox kenolaba kfouleggs kgoldrunner kjumpingcube klickety klines kmahjongg knetwalk kolf konquest kpat kpoker kreversi ksirtet ksnake ksmiletris kspaceduel ktron kwin4 lskat")
    kde.configure("--disable-setgid")

def build():
    kde.make()

def install():
    kde.install()
