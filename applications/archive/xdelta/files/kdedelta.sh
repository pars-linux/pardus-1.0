#!/bin/sh

KDE_MIRROR="ftp://ftp.kde.org/pub/kde/stable/"

KDE_OLD="3.4.92"
KDE_NEW="3.5.0"

ARTS_OLD="1.4.92"
ARTS_NEW="1.5.0"

KDE_PACKAGES="arts kdelibs kdebase kdenetwork kdepim kdeaccessibility kdeadmin kdeedu kdegames kdemultimedia kdetoys \
	      kdeaddons kdeartwork kdegraphics kdesdk kdeutils"

cd /var/cache/pisi/archives/

FTPDIR=${KDE_MIRROR}/${KDE_NEW}/src
echo -e "\n\n\033[01;37mStart download."

for name in $KDE_PACKAGES
do
	OLD=$KDE_OLD
	NEW=$KDE_NEW

	if [ $name == "arts" ]
	then
		OLD=$ARTS_OLD
		NEW=$ARTS_NEW
	fi

	OLDFILE=$name-${OLD}.tar
	NEWFILE=$name-${NEW}.tar
	DELTAFILE=$name-${OLD}-${NEW}.tar.xdelta
  
	if ! [ -f ${NEWFILE}.bz2 ]
	then 
		if [ -f ${OLDFILE}.bz2 ] 
		then
			if ! [ -f ${DELTAFILE} ]
			then
				echo -e "  \033[01;34m${DELTAFILE}\033[00m\n"
        		wget --passive-ftp ${FTPDIR}/$DELTAFILE 
			fi
		else
			echo -e "  \033[01;31m${OLDFILE}.bz2 is not in /var/cache/pisi/archives/ - downloading complete file instead of xdelta"
        		echo -e "  \033[01;34m${name}-${NEW}.tar.bz2\033[00m"
        		wget ${FTPDIR}/$name-${NEW}.tar.bz2 
		fi
	fi
done


echo -e "\n\n\033[01;37mFinished download.\nPatching...\n"

for name in $KDE_PACKAGES
do
	OLD=$KDE_OLD
	NEW=$KDE_NEW

	if [ $name == "arts" ]
	then
		OLD=$ARTS_OLD
		NEW=$ARTS_NEW
	fi

	OLDFILE=$name-${OLD}.tar
	NEWFILE=$name-${NEW}.tar
	DELTAFILE=$name-${OLD}-${NEW}.tar.xdelta
  
	if [ -f $DELTAFILE ]
	then 
		echo -e "\033[01;31mPatching \033[01;34m${OLDFILE}.bz2 \033[01;31mto \033[01;34m${NEWFILE}.bz2\033[00m\n\n"
    		bunzip2 $OLDFILE.bz2
        	xdelta patch $DELTAFILE $OLDFILE $NEWFILE
        	bzip2 $OLDFILE
        	bzip2 $NEWFILE
			rm -f $DELTAFILE
	fi
done
