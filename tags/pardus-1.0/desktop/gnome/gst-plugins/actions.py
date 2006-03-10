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
from pisi.actionsapi import get

def setup():

    # Full plugin list for gstreamer...
    plugins = ("a52dec", "aalib", "aalibtest", "alsa", "arts", "artsc", \
               "artstest", "audiofile", "audioresample", "cairo", "cdaudio", \
               "cdparanoia", "cdrom", "dirac", "directfb", "divx", "dts", "dv1394", \
               "dvdnav", "dvdread", "dxr3", "esd", "esdtest", "faac", "faad", "flac", \
               "freetypetest", "gconf", "gconftool", "gdk_pixbuf", "gnome_vfs", "gsm", \
               "gst_v4l", "gst_v4l2", "hermes", "ivorbis", "jack", "jpeg", "ladspa", "lame", \
               "lcs", "libcaca", "libdv", "libfame", "libfametest", "libmikmodtest", "libmms", \
               "libmng", "libpng", "librfb", "libtool-lock", "libvisual", "mad", "mikmod", \
               "mpeg2dec", "mpeg2enc", "mplex", "musepack", "musicbrainz", "nas", "nls", \
               "ogg", "oggtest", "opengl", "oss", "osx_audio", "osx_video", "pango", "polyp", "qcam", \
               "rpath", "sdl", "sdltest", "shout", "shout2", "shout2test", "sidplay", "smoothwave", "sndfile", "speex", "sunaudio", "swfdec", \
               "tarkin", "theora", "vcd", "vorbis", "vorbistest", "x", "xshm", "xvid", "xvideo")
    
    # Enabled plugins...
    enabled_plugins = ("theora", "vorbis", "ogg", "alsa", "oss", "x", "xshm", "mad")

    args = ""
    for plugin in plugins:
        if plugin not in enabled_plugins:
            args += "--disable-%s " % plugin
        else:
            args += "--enable-%s " % plugin

    autotools.configure(args)

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README")
