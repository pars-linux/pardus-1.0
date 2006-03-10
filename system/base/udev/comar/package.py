#!/usr/bin/python

import os
import time

def postInstall():
    if not os.path.exists("/var/tmp/pisi/udev_post_tmp"):
        os.makedirs("/var/tmp/pisi/udev_post_tmp")

    os.popen("/bin/mount --bind / /var/tmp/pisi/udev_post_tmp")
    os.chdir("/var/tmp/pisi/udev_post_tmp")

    if not os.path.exists("dev/null"):
        os.popen("mknod --mode=666 dev/null c 1 3")
    if not os.path.exists("dev/console"):
        os.popen("mknod dev/console c 5 1")
    if not os.path.exists("dev/tty1"):
        os.popen("mknod dev/tty1 c 4 1")

    os.chdir("/var/tmp/")
    os.popen("/bin/umount /var/tmp/pisi/udev_post_tmp")
    os.rmdir("/var/tmp/pisi/udev_post_tmp")

    os.popen("/usr/bin/killall -15 udevd &>/dev/null")
    time.sleep(1)
    os.popen("/usr/bin/killall -9 udevd &>/dev/null")
