#!/sbin/runscript
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

opts="${opts} reload debug"

depend() {
	need mdnsd
}

start() {
	if [ ! -f "/etc/mDNSResponderPosix.conf" ]; then
		eerror "You need to setup /etc/mDNSResponderPosix.conf first"
		return 1
	fi

	ebegin "Starting mDNSResponderPosix"
	start-stop-daemon --start --quiet --pidfile /var/run/mDNSResponderPosix.pid \
		--exec /usr/sbin/mDNSResponderPosix \
		-- -b -f /etc/mDNSResponderPosix.conf -P /var/run/mDNSResponderPosix.pid \
		$RESPONDER_ARGS

	eend $? "Failed to start mDNSResponderPosix"
}

stop() {
	ebegin "Stopping mDNSResponderPosix"
	start-stop-daemon --stop --quiet --pidfile /var/run/mDNSResponderPosix.pid
	eend $? "Failed to stop mDNSResponderPosix"
}

reload() {
	ebegin "Reloading mDNSResponderPosix"
	kill -HUP `cat /var/run/mDNSResponderPosix.pid` >&/dev/null
	eend $? "Failed to reload mDNSResponderPosix"
}

debug() {
	ebegin "Changing verbosity of mDNSResponderPosix"
	kill -USR1 `cat /var/run/mDNSResponderPosix.pid` >&/dev/null
	eend $? "Failed to change verbosity"
}
