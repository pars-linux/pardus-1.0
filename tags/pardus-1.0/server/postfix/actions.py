#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/util/sys_defs.h", "hash:\/etc\/aliases", "hash:/etc/mail/aliases")

def build():
    cc_args = "-DHAS_PCRE -DHAS_MYSQL -I/usr/include/mysql -DUSE_TLS -DUSE_SASL_AUTH \
               -I/usr/include/sasl"
    cc_libs = "-Wl,-z,now -L/usr/lib -lpcre -lcrypt -lpthread -lpam -lssl -lcrypto -lsasl2 -lmysqlclient -lm -lz"

    # Don't ask...
    pisitools.dosed("src/global/mail_params.h", \
                    "#define DEF_README_DIR\s+\"no\"", \
                    "#define DEF_README_DIR \"/usr/share/doc/%s/readme\"" % get.srcTAG())

    pisitools.dosed("src/global/mail_params.h", \
                    "#define DEF_HTML_DIR\s+\"no\"", \
                    "#define DEF_HTML_DIR \"/usr/share/doc/%s/html\"" % get.srcTAG())

    pisitools.dosed("src/global/mail_params.h", \
                    "#define DEF_MANPAGE_DIR\s+\"/usr/local/man\"", \
                    "#define DEF_MANPAGE_DIR \"/usr/share/man\"")

    pisitools.dosed("src/util/sys_defs.h", \
                    "#define NATIVE_DAEMON_DIR \"/usr/libexec/postfix\"", \
                    "#define NATIVE_DAEMON_DIR \"/usr/lib/postfix\"")

    autotools.make("CC=%s \
                    OPT=\"%s\" \
                    CCARGS=\"%s\" \
                    AUXLIBS=\"%s\" makefiles" % (get.CC(), get.CFLAGS(), cc_args, cc_libs))
    autotools.make()

def install():
    shelltools.system("/bin/sh postfix-install \
                       -non-interactive \
                       install_root=\"%(installDIR)s\" \
                       config_directory=\"/usr/share/doc/%(srcTAG)s/defaults\" \
                       readme_directory=\"/usr/share/doc/%(srcTAG)s/readme\" \
                       " % {'installDIR': get.installDIR(), 'srcTAG': get.srcTAG()})

    pisitools.removeDir("/var/")
    pisitools.dodir("/var/spool/postfix/")
    
    pisitools.dodir("/var/spool/mail/")
    pisitools.dosym("/var/spool/mail", "/var/mail")

    pisitools.dobin("auxiliary/rmail/rmail")

    pisitools.domove("/usr/sbin/sendmail", "/usr/sbin/sendmail.postfix")
    pisitools.domove("/usr/bin/rmail", "/usr/bin/rmail.postfix")
    pisitools.remove("/usr/bin/mailq")
    pisitools.remove("/usr/bin/newaliases")

    pisitools.domove("/usr/share/man/man1/sendmail.1", "/usr/share/man/man1", "sendmail-postfix.1")
    pisitools.domove("/usr/share/man/man1/newaliases.1", "/usr/share/man/man1", "newaliases-postfix.1")
    pisitools.domove("/usr/share/man/man1/mailq.1", "/usr/share/man/man1", "mailq-postfix.1")
    pisitools.domove("/usr/share/man/man5/aliases.5", "/usr/share/man/man5", "aliases-postfix.5")

    pisitools.dobin("auxiliary/qshape/qshape.pl")

    pisitools.dodir("/etc/mail/")
    pisitools.dodir("/etc/postfix/")

    pisitools.domove("/usr/share/doc/%s/defaults/*.cf" % get.srcTAG(), "/etc/postfix/")
    pisitools.domove("/usr/share/doc/%s/defaults/post*-*" % get.srcTAG(), "/etc/postfix/")

    pisitools.domove("examples/", "/usr/share/doc/%s/" % get.srcTAG())
    pisitools.dodoc("*README", "COMPATIBILITY", "HISTORY", "INSTALL", \
                    "LICENSE", "PORTING", "RELEASE_NOTES*")
    pisitools.dohtml("html/*")

    pisitools.dosym("pop", "/etc/pam.d/pop3")
    pisitools.dosym("pop", "/etc/pam.d/pop3s")
    pisitools.dosym("pop", "/etc/pam.d/pops")
    pisitools.dosym("imap", "/etc/pam.d/imap4")
    pisitools.dosym("imap", "/etc/pam.d/imap4s")
    pisitools.dosym("imap", "/etc/pam.d/imaps")
