#!/sbin/runscript
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

opts="${opts} reload"

depend() {
	need localmount
}

checkconfig() {
	if [ ! -e /proc/acpi ]; then
		eerror "ACPI support has not been compiled into the kernel"
		return 1
	fi
}

start() {
	checkconfig || return 1

	ebegin "Starting acpid"
	start-stop-daemon --start --quiet --exec /usr/sbin/acpid -- \
		-c /etc/acpi/events
	eend ${?}
}

stop() {
	ebegin "Stopping acpid"
	start-stop-daemon --stop --quiet --exec /usr/sbin/acpid
	eend ${?}
}

reload() {
	ebegin "Reloading acpid configuration"
	start-stop-daemon --stop --quiet --exec /usr/sbin/acpid --signal HUP
	eend ${?}
}
