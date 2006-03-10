#!/sbin/runscript
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

opts="${opts} dump"

depend() {
	after named
}

start() {
	if [ -z "${DNSEXTD_ZONE}" -o -z "${DNSEXTD_NAMESERVER}" ]; then
		eerror "You need to setup DNSEXTD_ZONE and DNSEXTD_NAMESERVER in /etc/conf.d/dnsextd first"
		return 1
	fi

	ebegin "Starting dnsextd"
	start-stop-daemon --start --quiet --user named \
		--pid /var/run/dnsextd.pid --exec /usr/sbin/dnsextd \
		-- -z "${DNSEXTD_ZONE}" -s "${DNSEXTD_NAMESERVER}" ${DNSEXTD_ARGS}

	eend $? "Failed to start dnsextd"
}

stop() {
	ebegin "Stopping dnsextd"
	start-stop-daemon --stop --quiet --pid /var/run/dnsextd.pid
	eend $? "Failed to stop dnsextd"
}

dump() {
	ebegin "Dumping dnsextd lease table"
	kill -INFO `cat /var/run/dnsextd.pid` >&/dev/null
	eend $? "Failed to dump dnsextd lease table"
}
