# PISI (Beta2) completion by Bahadır Kandemir <bahadir@haftalik.net>
# version: 0.1 (2005.11.20)

_pisi()
{
    local cur
    local commands commands2 options
    local options_build options_install options_upgrade

    # Commands
    commands="add-repo build build-build build-install \
              build-package build-setup build-unpack \
              build-until clean configure-pending \
              delete-cache graph help index info \
              install list-available list-components \
              list-installed list-pending list-repo \
              list-upgrades rebuild-db remove \
              remove-repo search-file update-repo \
              upgrade"
    commands2="--version --help"

    # Common options
    options="--verbose --debug --no-color --yes-all \
             --destdir= --username= --password="

    # Build options
    options_build="--ignore-build-no --ignore-action-errors \
                   --ignore-dependency --output-dir="
    

    # Install options
    options_build="--ignore-comar --bypass-safety \
                   --ignore-dependency --bypass-ldconfig \
                   --ignore-build-no"
    
    # Upgrade options
    options_upgrade="--eager"

    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    cur_num=${#COMP_WORDS[*]}

    if [[ ${cur_num} == 2  ]] && [[ ${cur} == --* ]]; then
    
        COMPREPLY=($(compgen -W "--help --version" -- ${cur}))
    elif [[ ${cur_num} == 2 ]]; then
    
        COMPREPLY=($(compgen -W "${commands} ${commands2}" -- ${cur}))
    elif [[ ${cur_num} == 3 ]] && [[ ${COMP_WORDS[1]} == *help ]]; then
    
        COMPREPLY=($(compgen -W "${commands}" -- ${cur}))
    elif [[ "${cur}" == --* ]]; then
        if [[ ${COMP_WORDS[1]} == 'build' ]]; then
            COMPREPLY=($(compgen -W "${options_build} ${options}" -- ${cur}))
        elif [[ ${COMP_WORDS[1]} == 'install' ]] || [[ ${COMP_WORDS[1]} == 'upgrade' ]]; then
            COMPREPLY=($(compgen -W "${options_upgrade} ${options_install} ${options}" -- ${cur}))
        else
            COMPREPLY=($(compgen -W "${options}" -- ${cur}))
        fi
    fi
    
    return 0
}
complete -F _pisi -o default pisi
