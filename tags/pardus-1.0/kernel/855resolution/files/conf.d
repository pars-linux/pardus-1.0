# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

# Config file for /etc/init.d/855resolution

# Since 855resolution alters the video RAM of your 855 card, it must be run
# on every boot.
# In this file you set which modes are to be replaced with what by the init
# script. The syntax should be self-explaining.
# To find out which modes are available, use "855resolution -l".
# Remember to add 855resolution to your default runlevel:
# rc-update add 855resolution default

# e.g's (it seems for most people 5c defaults to "1920x1440", which
#   usually isn't used, so the example uses that one
replace[0]="5c"
with[0]="1400 1050"
#with[0]="1280 800"

# Uncomment these if you want to replace more modes:
#replace[1]="modenumber"
#with[1]="width height"
#replace[2]="modenumber"
#with[2]="width height"

