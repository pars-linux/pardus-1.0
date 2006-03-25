#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "qt-x11-free-3.3.5"

# Where to install
QTBASE = "/usr/qt/3"
# For which platform
PLATFORM = "linux-g++"

def define_global():
    shelltools.export("PATH", "%s/bin:%s" % (get.curDIR(), get.ENV("PATH")))
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))

def setup():
    define_global()

    # Yeah, we accept your licence :)
    pisitools.dosed("configure", "read acceptance", "acceptance=yes")

    # Qt has serios security issue, 
    # see http://bugs.gentoo.org/show_bug.cgi?id=75181 and http://www.gentoo.org/security/en/glsa/glsa-200503-01.xml
    pisitools.dosed("mkspecs/linux-g++/qmake.conf", "QMAKE_RPATH.*= -Wl,-rpath,", "QMAKE_RPATH\t=")

    # Set c/xxflags and ldflags
    pisitools.dosed("mkspecs/%s/qmake.conf" % PLATFORM, "QMAKE_CFLAGS_RELEASE.*=.*", "QMAKE_CFLAGS_RELEASE=%s" % get.CFLAGS())
    pisitools.dosed("mkspecs/%s/qmake.conf" % PLATFORM, "QMAKE_CXXFLAGS_RELEASE.*=.*", "QMAKE_CXXFLAGS_RELEASE=%s" % get.CXXFLAGS())
    pisitools.dosed("mkspecs/%s/qmake.conf" % PLATFORM, "QMAKE_LFLAGS_RELEASE.*=.*", "QMAKE_LFLAGS_RELEASE=%s" % get.LDFLAGS())
    
    autotools.rawConfigure("-sm \
                            -thread \
                            -pch \
                            -stl \
                            -system-libjpeg \
                            -verbose \
                            -largefile \
                            -qt-imgfmt-{jpeg,mng,png} \
                            -tablet \
                            -system-libmng \
                            -system-libpng \
                            -lpthread \
                            -xft \
                            -platform %s \
                            -xplatform %s \
                            -xrender \
                            -prefix %s \
                            -libdir %s/lib \
                            -fast \
                            -qt-gif \
                            -cups \
                            -enable-module=opengl \
                            -xinerama \
                            -system-zlib \
                            -ipv6 \
                            -no-sql-mysql \
                            -no-sql-psql \
                            -no-sql-ibase \
                            -plugin-sql-sqlite \
                            -no-sql-odbc \
                            -release \
                            -no-g++-exceptions \
                            -dlopen-opengl" % (PLATFORM, PLATFORM, QTBASE, QTBASE ))

def build():
    define_global()

    shelltools.export("SYSCONF", "%s/etc/settings" % QTBASE)
    autotools.make()

def install():
    define_global()
    
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Correct Makefile's
    pisitools.dosed("examples/Makefile", get.curDIR() , QTBASE)
    for file in shelltools.ls("examples/*/Makefile"):
        pisitools.dosed(file, get.curDIR() , QTBASE)
       
    pisitools.dosed("tutorial/Makefile", get.curDIR() , QTBASE)
    for file in shelltools.ls("tutorial/*/Makefile"):
        pisitools.dosed(file, get.curDIR() , QTBASE)
       
    # Move tutorial and example into QTBASE 
    pisitools.insinto(QTBASE, "tutorial")
    pisitools.insinto(QTBASE, "examples")

    # Correct .qmake.cache
    pisitools.insinto(QTBASE, ".qmake.cache")
    pisitools.dosed("%s/usr/qt/3/.qmake.cache" % get.installDIR(), get.curDIR() , QTBASE)
