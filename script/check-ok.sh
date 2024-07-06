#!/bin/bash

# Check if the machine is ready

msg="
\r\n ip:     `ip`
\r\n uname:  `uname -a`
\r\n uptime: `uptime`
"

echo -e $msg
echo Ok