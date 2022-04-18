#!/bin/bash

if ! pgrep -f 'ping.py'
then
    nohup python3 -u /home/pi/ping/ping.py > /home/pi/ping/ping.out 2>&1 &
fi

