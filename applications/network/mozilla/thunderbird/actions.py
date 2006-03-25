#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "mozilla"

def setup():
    shelltools.export("MOZ_CO_PROJECT", "mail")
    shelltools.export("BUILD_OFFICIAL", "1")
    shelltools.export("MOZILLA_OFFICIAL", "1")

    shelltools.export("WANT_AUTOCONF", "2.1")
    autotools.autoconf()

    # Mozilla has different approach for build itself
    # See http://www.mozilla.org/build/configure-build.html and mozconfig.patch

    # mv patched locale into right dir...
    shelltools.makedirs("../l10n/")
    shelltools.move("tr/", "../l10n/tr")

    autotools.configure()

def build():
    autotools.make()
    
def install():
    pisitools.insinto("/usr/lib/", "dist/bin", "MozillaThunderbird")
    
    # Thunderbird is piece of crap, you need myspell en-US files in every
    # locale else this piece of shit won't work
    pisitools.dodir("/usr/lib/MozillaThunderbird/components/myspell")
    shelltools.copy("extensions/spellcheck/locales/en-US/myspell/en-US.*", "%s/usr/lib/MozillaThunderbird/components/myspell" % get.installDIR())

    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
