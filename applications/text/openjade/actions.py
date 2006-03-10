#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    libtools.gnuconfig_update()
    shelltools.export("ALLOWED_FLAGS", "-O -O1 -O2 -pipe -g")
    shelltools.sym("config/configure.in", "configure.in")
    shelltools.export("SGML_PREFIX", "/usr/share/sgml")
    autotools.configure("--enable-http \
                         --enable-default-catalog=/etc/sgml/catalog \
                         --enable-default-search-path=/usr/share/sgml \
                         --libdir=/usr/lib \
                         --datadir=/usr/share/sgml/%s" % get.srcTAG())

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr")
    pisitools.dodir("/usr/lib")

    autotools.rawInstall("prefix=%s/usr \
                          libdir=%s/usr/lib \
                          datadir=%s/usr/share/sgml/%s "\
                          % (get.installDIR(),\
                             get.installDIR(),\
                             get.installDIR(),\
                             get.srcTAG()))

    pisitools.dosym("openjade", "/usr/bin/jade")
    pisitools.dosym("onsgmls", "/usr/bin/nsgmls")
    pisitools.dosym("osgmlnorm", "/usr/bin/sgmlnorm")
    pisitools.dosym("ospam", "/usr/bin/spam")
    pisitools.dosym("ospent", "/usr/bin/spent")
    pisitools.dosym("osx", "/usr/bin/sgml2xml")

    pisitools.insinto("/usr/share/sgml/%s" % get.srcTAG(), "dsssl/builtins.dsl") 

    pisitools.insinto("/usr/share/sgml/%s/dsssl" % get.srcTAG(), "dsssl/dsssl.dtd") 
    pisitools.insinto("/usr/share/sgml/%s/dsssl" % get.srcTAG(), "dsssl/style-sheet.dtd") 
    pisitools.insinto("/usr/share/sgml/%s/dsssl" % get.srcTAG(), "dsssl/fot.dtd")
    pisitools.insinto("/usr/share/sgml/%s/pubtext" % get.srcTAG(), "pubtext/*")

    pisitools.dodoc("COPYING", "NEWS", "README", "VERSION")
    pisitools.dohtml("doc/*.htm")

    pisitools.insinto("/usr/share/doc/%s/jadedoc" % get.srcTAG(), "jadedoc/*.htm")
    pisitools.insinto("/usr/share/doc/%s/jadedoc/images" % get.srcTAG(), "jadedoc/images/*")

    """
    FIXME:
    sgml-catalog_cat_include "/etc/sgml/${P}.cat" \
        "/usr/share/sgml/openjade-${PV}/catalog"
    sgml-catalog_cat_include "/etc/sgml/${P}.cat" \
        "/usr/share/sgml/openjade-${PV}/dsssl/catalog"
    sgml-catalog_cat_include "/etc/sgml/sgml-docbook.cat" \
        "/etc/sgml/${P}.cat"
    """

