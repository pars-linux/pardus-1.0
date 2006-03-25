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

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    
    autotools.autoconf()

    autotools.configure("--without-apxs \
                        --with-swig \
                        --with-ssl \
                        --with-berkeley-db \
                        --with-python \
                        --enable-nls \
                        --with-neon=/usr \
                        --with-apr=/usr/bin/apr-config \
                        --with-apr-util=/usr/bin/apu-config \
                        --disable-experimental-libtool \
                        --disable-mod-activation")

def build():
    autotools.make("external-all")
    autotools.make("local-all")
    autotools.make("SVN_APR_INCLUDES=\"-I/usr/include/apr-0\" swig-py")

    pisitools.dosed("svn-config", "@SVN_DB_[^@]*@")

def install():
    shelltools.export("PYTHON_DIR", "/usr/lib/%s" % get.curPYTHON())
    
    # install svn
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("svn-config")

    # install swig-py
    autotools.rawInstall("DESTDIR=%s DISTUTIL_PARAM=--prefix=%s LD_LIBRARY_PATH=\"-L%s/usr/lib\"" % \
                        (get.installDIR(), get.installDIR(), get.installDIR()), "install-swig-py")

    # Move py/c'into proper dir
    pisitools.domove("/usr/lib/svn-python/svn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/svn-python/libsvn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.removeDir("/usr/lib/svn-python")
 
    pisitools.insinto("/usr/bin/", "tools/backup/hot-backup.py", "svn-hot-backup")
    pisitools.insinto("/usr/bin/", "contrib/client-side/svn_load_dirs.pl", "svn-load-dirs")
 
    pisitools.dodoc("BUGS", "COMMITTERS", "COPYING", "HACKING", "INSTALL", "README" \
                   "CHANGES", "tools/xslt/svnindex.css", "tools/xslt/svnindex.xsl")

    pisitools.dohtml("doc/book/book/")
