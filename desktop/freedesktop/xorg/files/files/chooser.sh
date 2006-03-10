#!/bin/sh
# Copyright 1999-2004 Gentoo Foundation
# Distributed under the terms of the GNU General Public License, v2
# Author:  Martin Schlemmer <azarah@gentoo.org>
# $Header: /home/cvsroot/gentoo-x86/x11-base/xfree/files/4.3.99.8/chooser.sh,v 1.1 2003/07/11 22:54:09 spyderous Exp $

# If $XSESSION is "", source first /etc/conf.d/basic, and then /etc/rc.conf
if [ -z "${XSESSION}" ]
then
	[ -f /etc/conf.d/basic ] && source /etc/conf.d/basic
	[ -f /etc/rc.conf ] && source /etc/rc.conf
fi

# Find a match for $XSESSION in /etc/X11/Sessions
PARDUS_SESSION=""
for x in /etc/X11/Sessions/*
do
	if [ "`echo ${x##*/} | awk '{ print toupper($1) }'`" \
		= "`echo ${XSESSION} | awk '{ print toupper($1) }'`" ]
	then
		PARDUS_SESSION=${x}
		break
	fi
done

PARDUS_EXEC=""

if [ -n "${XSESSION}" ]; then
	if [ -f /etc/X11/Sessions/${XSESSION} ]; then
		if [ -x /etc/X11/Sessions/${XSESSION} ]; then
			PARDUS_EXEC="/etc/X11/Sessions/${XSESSION}"
		else
			PARDUS_EXEC="/bin/sh /etc/X11/Sessions/${XSESSION}"
		fi
	elif [ -n "${PARDUS_SESSION}" ]; then
		if [ -x "${PARDUS_SESSION}" ]; then
			PARDUS_EXEC="${PARDUS_SESSION}"
		else
			PARDUS_EXEC="/bin/sh ${PARDUS_SESSION}"
		fi
	else
		x=""
		y=""
		
		for x in "${XSESSION}" \
			"`echo ${XSESSION} | awk '{ print toupper($1) }'`" \
			"`echo ${XSESSION} | awk '{ print tolower($1) }'`"
		do
			# Fall through ...
			if [ -x "`which ${x} 2>/dev/null`" ]; then
				PARDUS_EXEC="`which ${x} 2>/dev/null`"
				break
			fi
		done

		# If all else fail, run twm
		PARDUS_EXEC="/usr/bin/twm"
	fi
fi

echo "${PARDUS_EXEC}"


# vim:ts=4
