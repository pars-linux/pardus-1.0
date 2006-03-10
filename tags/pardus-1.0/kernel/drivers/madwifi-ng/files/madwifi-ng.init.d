#!/sbin/runscript
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original concept from user contributed docs in www.madwifi.org

depend() {
	use net
	before net.ath0
}

start() {
	ebegin "Creating ath0 in station mode"
	/sbin/wlanconfig ath0 create wlandev wifi0 wlanmode sta
	eend $?
}

stop() {
	ebegin "Stopping ath0"
	/sbin/wlanconfig ath0 destroy
	eend $?
}

