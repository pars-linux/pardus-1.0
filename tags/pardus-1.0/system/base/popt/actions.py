#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools

WorkDir="popt-1.7"

def setup():
    autotools.configure("--with-nls")

def build():
    autotools.make()

def install():
    autotools.install()
