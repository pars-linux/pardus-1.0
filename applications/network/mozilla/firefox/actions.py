#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mozilla"

def setup():
    shelltools.export("MOZ_CO_PROJECT", "browser")
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
    pisitools.insinto("/usr/lib/", "dist/bin", "MozillaFirefox")

    pisitools.insinto("/usr/lib/MozillaFirefox", "dist/include/", "include")
    pisitools.insinto("/usr/lib/MozillaFirefox", "dist/idl/", "idl")
    
    # Nss/Ldap headers
    pisitools.insinto("/usr/lib/MozillaFirefox/include", "dist/public/nss/", "nss")
    pisitools.insinto("/usr/lib/MozillaFirefox/include", "dist/public/ldap/", "ldap")
    pisitools.insinto("/usr/lib/MozillaFirefox/include", "dist/public/ldap-private", "ldap-private")
    
    # Dirty hack to get some applications using this header running
    pisitools.dosym("/usr/lib/MozillaFirefox/include/necko/nsIURI.h", \
                    "/usr/lib/MozillaFirefox/include/nsIURI.h")

    # mozilla-nss.pc & mozilla-nspr.pc symlinks
    pisitools.dosym("/usr/lib/pkgconfig/firefox-nss.pc", \
                    "/usr/lib/pkgconfig/mozilla-nss.pc")
    pisitools.dosym("/usr/lib/pkgconfig/firefox-nspr.pc", \
                    "/usr/lib/pkgconfig/mozilla-nspr.pc")
    
    # Remove bookmarks    
    pisitools.remove("/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
    
    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
