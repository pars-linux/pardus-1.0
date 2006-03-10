# Config file for /etc/init.d/slmodemd

DEV=/dev/ttySL0
COUNTRY=TURKEY
GROUP=dialout
# the group should be kept in sync with:
# /etc/devfs.d/slmodem (devfs)
# /etc/udev/rules.d/55-slmodem.rules (udev)

# The following symlink will be created if uncommented
LN_DEV=/dev/modem

# Raise priority to reduce modem dropouts
NICE=-6

# ALSA Options:

# The following sets the ALSA (alsasound) init script to
# be a dependancy of the slmodem one. It does also provides
# ALSA support.
MODULE=alsa

# The modem hardware slot
# use "modem:0", "modem:1", etc.
# usually modem:1 is used
HW_SLOT=modem:1

# Non-ALSA OPTIONS:

# MODULE=slamr
# or
# MODULE=slusb
