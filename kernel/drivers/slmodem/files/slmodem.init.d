#!/sbin/runscript
# Copyright 1999-2005 Gentoo Foundation
# Distributed under the terms of the GNU General Public License, v2 or later

if [ "${MODULE}" = "alsa" ];
then
	needalsasound="alsasound"
fi
depend() {
	need logger $needalsasound
}


checkconfig() {
	if [ -z "${COUNTRY}" ]; then
		eerror "You need to config /etc/conf.d/slmodem first"
		return 1
	fi
}

function loadsalsa {
	ebegin "Starting slmodemd"
	start-stop-daemon --start --background --nicelevel=${NICE} --make-pidfile \
		--pidfile /var/run/slmodemd.pid --startas /usr/sbin/slmodemd \
		-- -country=${COUNTRY} -g=${GROUP} --alsa ${HW_SLOT}
	return ${?}
}

function loadsmodule {
	modprobe ${MODULE};
    
	if [ "$?" -gt 0 ]
	then
		eerror "Missing module. Please set up /etc/conf.d/slmodem"
		return 1;
    	fi

	if [ -z "${MDEV}" ]; then MDEV="/dev/${MODULE}0"; fi
	if [ ! -c "${MDEV}" ]; then mknod ${MDEV} c 242 0; fi

	if [ ! -c /dev/ppp ]; then mknod /dev/ppp c 108 0; fi

    	ebegin "Starting slmodemd"
	start-stop-daemon --start --background --nicelevel=${NICE} --make-pidfile \
		--pidfile /var/run/slmodemd.pid --startas /usr/sbin/slmodemd \
		-- -country=${COUNTRY} -g=${GROUP} ${MDEV}
	return ${?}
}

start() {

	checkconfig || return 1

	# either if we use alsa or not, the only thing we need is 
	# ttySL0, which is created by slmodemd when started (points to a pts)

	if [ "${MODULE}" == "alsa" ]; then
		loadsalsa
	else
		loadsmodule
	fi
    
	result=${?}
    
	test ! -z "${LN_DEV}" && /bin/ln -s ${DEV} ${LN_DEV} 2> /dev/null
    
	eend ${result}
}

stop() {
	ebegin "Shutting down slmodemd"
	start-stop-daemon --stop --quiet --pidfile /var/run/slmodemd.pid
	result=${?}
	[ -e /var/run/slmodemd.pid ] && rm /var/run/slmodemd.pid
	unlink ${LN_DEV} 2> /dev/null
	eend ${result}
	if [ ! "${MODULE}" == "alsa" ];
	then
		ebegin "Waiting for modem driver unload"
		if [ "$RC_NOCOLOR" != "yes" ]; then
			echo -e "\e[A\e[44G   "
			echo -ne "\e[A\e[44G"
		fi
		for ((a=0,result=1; result==1 && a <= 5 ; a++))
		do
			sleep 0.25
			echo -n "."
			modprobe -r slamr 2> /dev/null && result=0
		done
		if [ "$RC_NOCOLOR" != "yes" ]; then echo; fi
		eend ${result}
	fi
}
