#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@haftalik.net>

from pisi.actionsapi import pisitools

WorkDir = "bash_completion"

def install():
    pisitools.dosed("bash_completion", \
                    "complete -F _mount \$default \$filenames mount", \
                    "#complete -F _mount $default $filenames mount")
    pisitools.insinto("/etc", "bash_completion")

    pisitools.insinto("/usr/share/bash-completion", "contrib/*")

    pisitools.dodoc("Changelog", "README")
