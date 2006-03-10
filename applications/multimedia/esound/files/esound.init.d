#!/sbin/runscript
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

# Note: You need to start esound on boot, only if you want to use it over network.

# Warning: To use global esound daemon, you must also set spawn_options
# in /etc/esd/esd.conf to the same protocol (i. e. add "-tcp") and unset
# "Enable sound server startup" in gnome-sound-properties for all users
# and optionally handle authentization.

depend() {
	use net portmap alsasound
}

start() {
	ebegin "Starting esound"
	start-stop-daemon --start --quiet --background --exec /usr/bin/esd -- $ESD_START $ESD_OPTIONS
	eend $?
}

stop() {
	ebegin "Stopping esound"
	start-stop-daemon --stop --quiet --exec /usr/bin/esd
	eend $?
}
