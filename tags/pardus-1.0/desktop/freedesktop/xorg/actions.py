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

WorkDir = "xc"

def setup():
    host_def_setup()

def build():
    shelltools.export("FAST", "1")
  
    # Compile fix for stupid xorg's gcc.2.95 dependency
    shelltools.touch("programs/Xserver/hw/dmx/doc/dmx")
    shelltools.touch("programs/Xserver/hw/dmx/doc/dmx.ps")

    autotools.make("-j1 World WORLDOPTS=\"\" MAKE=\"make\"")

def install():
    autotools.install("MAKE=\"make\" DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("RELNOTES")

    # Backwards compatibility for /usr/share move
    pisitools.domove("/usr/lib/X11/fonts/encodings", "/usr/share/fonts")
    pisitools.removeDir("/usr/lib/X11/fonts/")
    pisitools.dosym("../../share/fonts", "/usr/lib/X11/fonts")
    
    # Fix permissions on locale/common/*.so
    for file in shelltools.ls("%s/usr/lib/X11/locale/lib/common/*.so*" % get.installDIR()):
        shelltools.chmod(file, 0755)
    
    # Fix permissions on modules
    for file in shelltools.ls("%s/usr/lib/modules/*.so" % get.installDIR()):
        shelltools.chmod(file, 0755)

    for file in shelltools.ls("%s/usr/lib/modules/*.o" % get.installDIR()):
        shelltools.chmod(file, 0755)

    shelltools.chmod("%s/usr/lib/X11/xkb/geometry/sgi" % get.installDIR(), 0755)
    shelltools.chmod("%s/usr/bin/dga" % get.installDIR(), 0755)

    # Standard symlinks
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")
    pisitools.dosym("../bin", "/usr/bin/X11")

    # Stop complains about "file or directory not existing"
    pisitools.dosym("../../usr/lib/X11/xkb", "/etc/X11/xkb")

    # Backwards compat, FHS, etc.
    pisitools.dosym("/usr/bin/Xorg", "/etc/X11/X")

    #Remove invalid symlinks
    pisitools.remove("/usr/lib/libGL.so")
    pisitools.remove("/usr/lib/libGL.so.1")

    #Create required symlinks
    pisitools.dosym("libGL.so.1.2", "/usr/lib/libGL.so")
    pisitools.dosym("libGL.so.1.2", "/usr/lib/libGL.so.1")

    # Moving libGL and friends for dynamic switching
    pisitools.dodir("/usr/lib/opengl/lib")
    pisitools.dodir("/usr/lib/opengl/extensions")
    pisitools.dodir("/usr/lib/opengl/include")

    for file in shelltools.ls("%s/usr/lib/libGL.so*" % get.installDIR()):
        pisitools.domove(file.replace(get.installDIR(), ""), "/usr/lib/opengl/xorg-x11/lib/")

    pisitools.domove("/usr/lib/libGL.la", "/usr/lib/opengl/xorg-x11/lib/")
    pisitools.domove("/usr/lib/libGL.a", "/usr/lib/opengl/xorg-x11/lib/")

    for file in shelltools.ls("%s/usr/lib/modules/extensions/libglx*" % get.installDIR()):
        pisitools.domove(file.replace(get.installDIR(), ""), "/usr/lib/opengl/xorg-x11/extensions/")

    for file in ("gl.h", "glx.h", "glxtokens.h", "glext.h", "glxext.h", "glxmd.h", "glxproto.h"):
        pisitools.domove("/usr/include/GL/%s" % file, "/usr/lib/opengl/xorg-x11/include")

    # RH-style init script, we provide a wrapper
    pisitools.doexe("/etc/init.d/xprint", "/usr/lib/misc/")
    pisitools.remove("/etc/init.d/xprint")

    # patch profile scripts
    pisitools.dosed("%s/etc/profile.d/xprint*" % get.installDIR(), \
                    "/bin/sh.*get_xpserverlist", \
                    "/usr/$(get_libdir)/misc/xprint get_xpserverlist")

    # Make the core cursor the default.
    pisitools.dosed("%s/usr/share/cursors/xorg-x11/default/index.theme" % get.installDIR(), "whiteglass", "Jimmac")

    #move profile scripts, we can't touch /etc/profile.d/
    pisitools.remove("/etc/profile.d/xprint*")

    #Remove the /etc/rc.d nonsense -- not everyone is RedHat
    pisitools.removeDir("/etc/rc.d")

    fnts, conf_example = "/usr/share/fonts", "%s/etc/X11/xorg.conf.example" % get.installDIR()

    # Fix default config files after installing fonts to /usr/share/fonts
    for x in ["/usr/lib/X11/fonts", "/usr/lib/fonts"]:
        pisitools.dosed(conf_example, x, fnts)

    # Make VERY sure X can compile keymaps
    pisitools.remove("/usr/lib/X11/xkb/compiled")
    pisitools.dosym("/tmp", "/usr/lib/X11/xkb/compiled")

    # silly rc3 bug...
    #pisitools.dosed("%s/usr/lib/pkgconfig/xft.pc" % get.installDIR(), "Requires: xproto, xrender, fontconfig, freetype2", "Requires: fontconfig, freetype2")

def host_def_setup():
    HOSTCONF = "config/cf/host.def"

    shelltools.echo(HOSTCONF, "#define XVendorString \"Pardus (The X.Org Foundation 6.9.0)\"")
    # FHS install locations
    shelltools.echo(HOSTCONF, "#define ManDirectoryRoot /usr/share/man")
    shelltools.echo(HOSTCONF, "#define DocDir /usr/share/doc/%s" % get.srcTAG())
    shelltools.echo(HOSTCONF, "#define FontDir /usr/share/fonts")
    shelltools.echo(HOSTCONF, "#define BinDir /usr/bin")
    shelltools.echo(HOSTCONF, "#define IncRoot /usr/include")
    shelltools.echo(HOSTCONF, "#define LibDir /usr/lib/X11")
    shelltools.echo(HOSTCONF, "#define UsrLibDir /usr/lib")
    shelltools.echo(HOSTCONF, "#define LinkGLToUsrInclude NO")

    # Make man4 and man7 stuff get 'x' suffix like everything else
    # Necessary so we can install to /usr/share/man without overwriting
    shelltools.echo(HOSTCONF, "#define DriverManDir \$(MANSOURCEPATH)4")
    shelltools.echo(HOSTCONF, "#define DriverManSuffix 4x /* use just one tab or cpp will die */")
    shelltools.echo(HOSTCONF, "#define MiscManDir \$(MANSOURCEPATH)7")
    shelltools.echo(HOSTCONF, "#define MiscManSuffix 7x /* use just one tab or cpp will die */")

    # Don't build xterm -- use external
    shelltools.echo(HOSTCONF, "#define BuildXterm NO")

    # Xwrapper has been removed so we now need to use the set uid server
    # again, this mustve happened somewhere after 4.3.0 in the development.
    shelltools.echo(HOSTCONF, "#define InstallXserverSetUID YES")
    shelltools.echo(HOSTCONF, "#define BuildServersOnly NO")

    shelltools.echo(HOSTCONF, "#define HaveLib64 NO")

    # Set location of DRM source to be installed
    shelltools.echo(HOSTCONF, "#define InstSrcDir /usr/src/%s" % get.srcTAG())

    shelltools.echo(HOSTCONF, "#define CcCmd %s" % get.CC())
    shelltools.echo(HOSTCONF, "#define OptimizedCDebugFlags %s GccAliasingArgs" % get.CFLAGS())
    shelltools.echo(HOSTCONF, "#define OptimizedCplusplusDebugFlags %s GccAliasingArgs" % get.CXXFLAGS())
    
    shelltools.echo(HOSTCONF, "#define DoLoadableServer  YES")
    shelltools.echo(HOSTCONF, "#define MakeDllModules    YES")
    
    # Use less RAM
    shelltools.echo(HOSTCONF, "#define GccWarningOptions -Wno-return-type -w")

    shelltools.echo(HOSTCONF, "#define HasPam YES")
    shelltools.echo(HOSTCONF, "#define HasPamMisc YES")

    # optimize Mesa for architecture
    shelltools.echo(HOSTCONF, "#define HasMMXSupport YES")
    shelltools.echo(HOSTCONF, "#define HasSSESupport YES")

    # Do we want the glx extension?
    shelltools.echo(HOSTCONF, "#define BuildGlxExt YES")
    shelltools.echo(HOSTCONF, "#define BuildGLXLibrary YES")
    shelltools.echo(HOSTCONF, "#define BuildXF86DRI YES")
    # Needs GL headers
    shelltools.echo(HOSTCONF, "#define BuildGLULibrary YES")

    # Make xv optional for more minimal builds
    shelltools.echo(HOSTCONF, "#define BuildXvLibrary YES")
    shelltools.echo(HOSTCONF, "#define BuildXvExt YES")
    # Depends on X11/extensions/Xv.h
    shelltools.echo(HOSTCONF, "#define BuildXF86RushExt YES")
    shelltools.echo(HOSTCONF, "#define BuildXF86RushLibrary YES")

    # The definitions for fontconfig
    shelltools.echo(HOSTCONF, "#define UseFontconfig YES")
    shelltools.echo(HOSTCONF, "#define HasFontconfig YES")

    # Use the xorg Xft2 lib
    shelltools.echo(HOSTCONF, "#define SharedLibXft YES")

    shelltools.echo(HOSTCONF, "#define BuildLinuxDocPS YES")
    shelltools.echo(HOSTCONF, "#define BuildSpecsDocs YES")
    shelltools.echo(HOSTCONF, "#define BuildHtmlManPages YES")
    shelltools.echo(HOSTCONF, "#define InstallHardcopyDocs YES")

    # Native Language Support Fonts
    shelltools.echo(HOSTCONF, "#define BuildCyrillicFonts NO")
    shelltools.echo(HOSTCONF, "#define BuildArabicFonts NO")
    shelltools.echo(HOSTCONF, "#define BuildGreekFonts NO")
    shelltools.echo(HOSTCONF, "#define BuildHebrewFonts NO")
    shelltools.echo(HOSTCONF, "#define BuildThaiFonts NO")

    # Crappy bitmap fonts
    shelltools.echo(HOSTCONF, "#define Build75DpiFonts YES")
    shelltools.echo(HOSTCONF, "#define Build100DpiFonts YES")

    # Type1 fonts
    shelltools.echo(HOSTCONF, "#define BuildType1Fonts YES")

    # TrueType fonts
    shelltools.echo(HOSTCONF, "#define BuildTrueTypeFonts YES")

    # Distributed Multiheaded X
    shelltools.echo(HOSTCONF, "#define BuildDmx YES")

    shelltools.echo(HOSTCONF, "#define BuildXprint YES")
    shelltools.echo(HOSTCONF, "#define BuildXprintClients YES")

    shelltools.echo(HOSTCONF, "#define BuildFontServer NO")    
