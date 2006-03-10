#!/sbin/runscript
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

opts="${opts} reload dump"

depend() {
	after net
}

start() {
	ebegin "Starting mdnsd"
	start-stop-daemon --start --quiet --pidfile /var/run/mdnsd.pid \
		--exec /usr/sbin/mdnsd

	eend $? "Failed to start mdnsd"
}

stop() {
	ebegin "Stopping mdnsd"
	start-stop-daemon --stop --quiet --pidfile /var/run/mdnsd.pid
	eend $? "Failed to stop mdnsd"
}

reload() {
	ebegin "Reloading mdnsd"
	kill -HUP `cat /var/run/mdnsd.pid` >&/dev/null
	eend $? "Failed to reload mdnsd"
}

dump() {
	ebegin "Dump mdnsd state to logs"
	kill -USR1 `cat /var/run/mdnsd.pid` >&/dev/null
	eend $? "Failed to dump mdnsd state"
}
