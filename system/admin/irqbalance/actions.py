 #!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Timu EREN <selamtux@gmail.com>
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "irqbalance"

def build():
    autotools.make()

def install():
   pisitools. dosbin("irqbalance")

   pisitools.doman("irqbalance.1")

   pisitools.dodoc("Changelog", "TODO")
