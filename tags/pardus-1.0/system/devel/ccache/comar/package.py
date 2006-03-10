#!/usr/bin/python

import os

def postInstall():
    try:
        os.makedirs("/root/.ccache")
    except OSError:
        pass

    # set maximum cache size to 2GB
    os.system("/usr/bin/ccache -M 2G")

    # create links
    os.system("/usr/bin/ccache-config --install-links")
    os.system("/usr/bin/ccache-config --install-links i686-pc-linux-gnu")
