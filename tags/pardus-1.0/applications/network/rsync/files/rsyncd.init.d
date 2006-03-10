#!/sbin/runscript
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

depend() {
	use net
}

start() {
	ebegin "Starting rsyncd"
	rsync --daemon ${RSYNC_OPTS}
	eend $?
}

stop() {
	ebegin "Stopping rsyncd"
	start-stop-daemon --stop --pidfile /var/run/rsyncd.pid
	eend $?
}
