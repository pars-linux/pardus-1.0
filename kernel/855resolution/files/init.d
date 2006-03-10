#!/sbin/runscript
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Original work belongs Gentoo Linux

depend() {
	before xdm
}

checkconfig() {
	if [ -z "${replace[0]}" ] || [ -z "${with[0]}" ]
	then
		eerror "You need to set at least one replace/with pair in /etc/conf.d/855resolution"
		return 1
	fi
}

start() {
	checkconfig || return 1

	ebegin "Running 855resolution to replace ${#replace[@]} mode(s)"
	i=0; return=0; retval=0
	for target in "${replace[@]}"
	do
		/usr/sbin/855resolution $target ${with[$i]} > /dev/null
		retval=$?
		if [ "$retval"!=0 ]; then return=$retval; fi
		i=$(($i+1))
	done
	eend $return
}

