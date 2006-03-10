#!/bin/bash

discover=/usr/bin/discover

types=$*

module_details=$(${discover} --data-path=linux/module/name --data-path=linux/module/options --format="%s %s" --data-version=`uname -r` ${types} | egrep -v '^ *$')

# Poor man's uniq.
module_details_uniq=""
for module_info in ${module_details}; do
	echo ${module_details_uniq} | grep ${module_info} > /dev/null 2>&1
	if [ $? -eq 1 ]; then
		module_details_uniq="${module_details_uniq} ${module_info}"
    fi
done
module_details=${module_details_uniq}

# Print module names
for module_info in ${module_details}; do
	module_name=$(echo ${module_info} | sed 's/^\([^ ]\+\).*/\1/')
	echo $module_name
done
