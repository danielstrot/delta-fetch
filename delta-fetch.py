#!/usr/bin/env python

# legal bullshit:
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2017 rfk1ll <rfk1lldev@gmail.com>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.


from os import getlogin, uname
import socket
import subprocess

#Read and process the uptime from proc
try:
    with open('/proc/uptime', 'r') as f:
        uptimeRaw = float(f.readline().split()[0])
        uptimeDays = int(uptimeRaw / 86400)
        uptimeHours = int((uptimeRaw % 86400) / 3600)
        uptimeMinutes = int((uptimeRaw % 3600) / 60)
except IOError as e:
    print("error: Could not read /proc/uptime.")
    exit(e)

#Set some variables for substitions in the logo
unameInfo = uname()
#username = getlogin()
#hostname = unameInfo[1]


#Print the logo
print("""
     :MNhhhhhhhhhhhhhhhhhhhhhhhNN.
      /No       MMMMMMM     `ym-
       :Ny`     | _ / |    .dd.
        .dh`    | 0 0 |   :my`
         `hd.    \_O_/   +No
          `sm:     |    `sm:
            oN/        .hd-
             /No      -my`
              :my`   /No`
               .dh` oN/
                `hmhm-
                 `sy.
     }}}}} 00:DE:AD:BE:EF:00 {{{{{
""")
process = subprocess.Popen("iwconfig", stdout=subprocess.PIPE)
stdout_iterator = iter(process.stdout.readline, b"")


for line in stdout_iterator:
    if line.decode("utf-8")[0].isalnum():
        print(line.decode("utf-8").strip())

    if "Mode:Monitor" in line.decode("utf-8"):
        print("\t  " + line.decode("utf-8").strip())
        print("          |==|injection*ready|>-----")
    elif "Mode:" in line.decode("utf-8"):
        print("\t  " + line.decode("utf-8").strip())
#print("""          Operating System: Arch Linux
#          Uptime: %(uptimeDays)s days, %(uptimeHours)s hours, %(uptimeMinutes)s minutes
#""" % locals())
