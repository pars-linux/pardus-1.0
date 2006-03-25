#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # Remove autoconf dependency
    pisitools.dosed("Makefile.in", "&& autoconf")

    # Enable SSH_SOURCE_BASHRC
    shelltools.echo("config-top.h", "#define SSH_SOURCE_BASHRC")
    # Enable system-wide bashrc 
    shelltools.echo("config-top.h", "#define SYS_BASHRC \"/etc/bash/bashrc\"")
    # Enable system-wide logout
    shelltools.echo("config-top.h", "#define SYS_BASH_LOGOUT \"/etc/bash/bash_logout\"")

    # Force pgrp synchronization
    # (https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=81653)
    #
    # The session will hang cases where you 'su' (not 'su -') and
    # then run a piped command in emacs.
    # This problem seem to happen due to scheduler changes kernel
    # side - although reproduceble with later 2.4 kernels, it is
    # especially easy with 2.6 kernels.
    shelltools.echo("config-bot.h", "#define PGRP_PIPE 1")

    pisitools.dosed("configure", "-lcurses", "-lncurses")

    autotools.configure("--with-nls --disable-profiling --without-gnu-malloc --with-ncurses")

    # Make sure we always link statically with ncurses
    pisitools.dosed("Makefile", "(?m)^(TERMCAP_LIB.*)-lncurses", r"\1-Wl,-Bstatic -lncurses -Wl,-Bdynamic")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.domove("/usr/bin/bash", "/bin")
    pisitools.dosym("/bin/bash","/bin/sh")
    pisitools.dosym("/bin/bash","/bin/rbash")
    pisitools.dodoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
    pisitools.doman("doc/bash.1", "doc/bashbug.1", "doc/builtins.1", "doc/rbash.1")
    pisitools.dosym("bash.info", "/usr/share/info/bashref.info")
