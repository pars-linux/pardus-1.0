#!/usr/bin/python

import os
import shutil

def postInstall():

    os.system("/usr/bin/install-catalog --add \
                      /etc/sgml/sgml-ent.cat \
                      /usr/share/sgml/sgml-iso-entities-8879.1986/catalog")

    os.system("/usr/bin/install-catalog --add \
                     /etc/sgml/sgml-docbook.cat \
                     /etc/sgml/sgml-ent.cat")

