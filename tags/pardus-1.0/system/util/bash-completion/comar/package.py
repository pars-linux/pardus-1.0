#!/usr/bin/python

def postInstall():
    f = open("/etc/profile", "a")
    f.write("\n# Bash-completion\n")
    f.write("[ -f /etc/profile.d/bash-completion ] && source /etc/profile.d/bash-completion\n")
    f.close()
