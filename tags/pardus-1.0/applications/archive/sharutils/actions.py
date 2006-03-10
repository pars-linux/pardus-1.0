#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("po/nl.po", "aangemaakt", "aangemaakt\\\\n")
    pisitools.dosed("po/pt.po", "de %dk", "de %dk\\\\n")

    autotools.configure("--enable-nls")
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.doman("doc/*.[15]")
    pisitools.dodoc("AUTHORS", "BACKLOG", "ChangeLog", "ChangeLog.OLD", \
                    "NEWS", "README", "README.OLD", "THANKS", "TODO")

    for dir in ("/usr/share/locale/de.", "/usr/share/locale/fr.", "/usr/share/locale/nl.", "/usr/share/locale/pt.", "/usr/share/locale/sv."):
        pisitools.removeDir(dir)

    pisitools.removeDir("/usr/lib")
