#!/usr/bin/python

import os
import shutil
import glob

def postInstall():
    exists = os.path.exists

    if not exists("/boot/grub"):
        os.makedirs("/boot/grub")

    if not exists("/boot/grub/grub.conf") and exists("/boot/grub/menu.lst"):
        shutil.move("/boot/grub/menu.lst", "/boot/grub/grub.conf")

    if not exists("/boot/grub/menu.lst"):
        os.symlink("grub.conf", "/boot/grub/menu.lst")

    if exists("/boot/grub/stage2"):
        shutil.move("/boot/grub/stage2", "/boot/grub/stage2.old")

    # "Copying files from /lib/grub and /usr/lib/grub to /boot"
    fnlist = glob.glob("/lib/grub/*/*")
    fnlist2 = glob.glob("/usr/lib/grub/*/*")
    for x in fnlist2: fnlist.append(x)

    for x in fnlist:
        if os.path.isfile(x):
            fname = os.path.basename(x)
            newpath = os.path.join("/boot/grub", fname)
            shutil.copyfile(x, newpath)


    if exists("/boot/grub/grub.conf"):
        cmd = "/sbin/grub --batch --device-map=/boot/grub/device.map < /boot/grub/grub.conf > /dev/null 2>&1"
        os.system(cmd)
