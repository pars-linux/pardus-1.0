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

WorkDir = "httpd-2.0.55"

def setup():
    shelltools.export("LC_CTYPE", "C")

    shelltools.echo("config.layout", config_layout())
    pisitools.dosed("config.layout", "version", get.srcTAG())
    
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.system ("./buildconf")

    shelltools.echo("config.cache", "ac_cv_func_sem_open=${ac_cv_func_sem_open=no}")

    autotools.rawConfigure("--with-mpm=prefork \
                            --enable-layout=Pardus \
                            --with-ssl=/usr \
                            --enable-ssl=shared \
                            %s \
                            --with-perl=/usr/bin/perl \
                            --with-expat=/usr \
                            --with-z=/usr \
                            --with-port=80 \
                            --with-program-name=apache2 \
                            --with-devrandom=/dev/urandom \
                            --with-apr=/usr/bin/apr-config \
                            --with-apr-util=/usr/bin/apu-config \
                            --cache-file=config.cache \
                            --with-suexec-safepath=\"/usr/bin:/bin\" \
                            --with-suexec-logfile=/var/log/apache2/suexec_log \
                            --with-suexec-bin=/usr/sbin/suexec2 \
                            --with-suexec-userdir=\"public_html\" \
                            --with-suexec-caller=apache \
                            --with-suexec-docroot=/var/www \
                            --with-suexec-uidmin=1000 \
                            --with-suexec-gidmin=100 \
                            --with-suexec-umask=077 \
                            --enable-suexec=shared" % modules_config())

    shelltools.touch("modules/ssl/ssl_expr_scan.c")

    pisitools.dosed("include/ap_config_auto.h", "apache2\.conf", "httpd.conf")

def build():
    autotools.make()

    shelltools.cd("support/")

    shelltools.unlinkDir("ab")
    #shelltools.unlink(".libs/ab")
    shelltools.unlink("ab.lo")
    shelltools.unlink("ab.o")

    autotools.make("ab CFLAGS=\"%s -DUSE_SSL -lcrypto -lssl -I/usr/include/openssl -L/usr/lib\"" % get.CFLAGS())

    shelltools.move("ab", "ab-ssl")
    shelltools.unlink("ab.lo")
    shelltools.unlink("ab.o")

    autotools.make("ab")

    shelltools.cd("../")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("dodoc", "ABOUT_APACHE", "CHANGES", "INSTALL", "LAYOUT", "LICENSE", "README*")

    pisitools.dosym("/usr/lib", "/usr/lib/apache2/lib")
    pisitools.dosym("/var/log/apache2", "/usr/lib/apache2/logs")
    pisitools.dosym("/etc/apache2", "/usr/lib/apache2/conf")

    pisitools.dosbin("support/split-logfile")
    pisitools.dosbin("support/list_hooks.pl")
    pisitools.dosbin("support/logresolve.pl")
    pisitools.dosbin("support/log_server_status")

    pisitools.dosbin("support/ab-ssl")
    pisitools.dosbin("apache2")

    # Tidy
    pisitools.domove("/usr/sbin/apachectl", "/usr/sbin", "apachec2tl")
    pisitools.domove("/usr/sbin/list_hooks.pl", "/usr/sbin", "list_hooks2.pl")
    pisitools.domove("/usr/sbin/logresolve.pl", "/usr/sbin", "logresolve2.pl")
    pisitools.domove("/usr/sbin/ab-ssl", "/usr/sbin", "ab2-ssl")
    pisitools.domove("/usr/sbin/suexec", "/usr/sbin", "suexec2")

    for i in ["htdigest", "htpasswd", "logresolve", "apxs",
              "ab", "rotatelogs", "dbmmanage", "checkgid",
              "split-logfile"]:
        pisitools.domove("/usr/sbin/%s" % i, "/usr/sbin", "%s2" % i)

    for i in ["htdigest", "htpasswd", "dbmmanage"]:
        pisitools.domove("/usr/share/man/man1/%s.1" % i, "/usr/share/man/man1", "%s2.1" % i)

    for i in ["ab", "apxs", "logresolve", "rotatelogs"]:
        pisitools.domove("/usr/share/man/man8/%s.8" % i, "/usr/share/man/man8", "%s2.8" % i)

    pisitools.domove("/usr/share/man/man8/apachectl.8", "/usr/share/man/man8", "apache2ctl.8")
    pisitools.domove("/usr/share/man/man8/httpd.8", "/usr/share/man/man8", "apache2.8")
    pisitools.domove("/usr/share/man/man8/suexec.8", "/usr/share/man/man8", "suexec2.8")

    pisitools.dodoc("/etc/apache2/*-std.conf")
    
    pisitools.domove("/usr/sbin/envvars*", "/usr/lib/apache2/build")
    pisitools.dosed("%s/usr/sbin/apxs2" % get.installDIR(), \
                    "my \$envvars = get_vars\(\"sbindir\"\) \. \"/envvars\";", \
                    "my $envvars = \"$installbuilddir/envvars\";")

    # Clean-up
    pisitools.remove("/etc/apache2/*")
    pisitools.remove("/var/www/localhost/htdocs/*")
    
    # Add conf.d for 3rd party configuration files
    pisitools.dodir("/etc/apache2/conf.d")

def config_layout():
    return """<Layout Pardus>
    prefix:          /usr
    exec_prefix:     /usr
    bindir:          /usr/bin
    sbindir:         /usr/sbin
    libdir:          /usr/lib
    libexecdir:      /usr/lib/apache2/modules
    mandir:          /usr/share/man
    infodir:         /usr/share/info
    includedir:      /usr/include/apache2
    installbuilddir: /usr/lib/apache2/build
    datadir:         /var/www/localhost
    errordir:        /var/www/localhost/error
    iconsdir:        /var/www/localhost/icons
    htdocsdir:       /var/www/localhost/htdocs
    cgidir:          /var/www/localhost/cgi-bin
    manualdir:       /usr/share/doc/version/manual
    sysconfdir:      /etc/apache2
    localstatedir:   /var
    runtimedir:      /var/run
    logfiledir:      /var/log/apache2
    proxycachedir:   /var/cache/apache2
</Layout>
"""
    
def modules_config():
    modname = (lambda x: x.replace("mod_", ""))

    disabled = ['mod_example', 'mod_optional-hook-export',
                'mod_optional-hook-import', 'mod_optional-fn-import',
                'mod_optional-fn-export', 'mod_bucketeer']
    static = ['mod_so']
    shared = ['mod_access', 'mod_auth', 'mod_auth_dbm',
              'mod_auth_anon', 'mod_auth_digest', 'mod_alias',
              'mod_file-cache', 'mod_echo', 'mod_charset-lite',
              'mod_cache', 'mod_disk-cache', 'mod_mem-cache',
              'mod_ext-filter', 'mod_case_filter', 'mod_case-filter-in',
              'mod_deflate', 'mod_mime-magic', 'mod_cern-meta',
              'mod_expires', 'mod_headers', 'mod_usertrack',
              'mod_unique-id', 'mod_proxy', 'mod_proxy-connect',
              'mod_proxy-ftp', 'mod_proxy-http', 'mod_info',
              'mod_include', 'mod_cgi', 'mod_cgid', 'mod_dav',
              'mod_dav-fs', 'mod_vhost-alias', 'mod_speling',
              'mod_rewrite', 'mod_log_config', 'mod_logio',
              'mod_env', 'mod_setenvif', 'mod_mime',
              'mod_status', 'mod_autoindex', 'mod_asis',
              'mod_negotiation', 'mod_dir', 'mod_imap',
              'mod_actions', 'mod_userdir']

    conf = ""

    for i in disabled:
        conf += "--disable-%s " % modname(i)
    for i in static:
        conf += "--enable-%s=yes " % modname(i)
    for i in shared:
        conf += "--enable-%s=shared " % modname(i)

    return conf
