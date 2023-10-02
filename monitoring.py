#!/usr/bin/python3
from datetime import date
import json
import os.path
import time

# Set file path and name
path = "/var/log"
filedate = str(date.fromtimestamp(time.time()))
filename = "-awesome-monitoring.log"
logfilename = os.path.join(path, filedate + filename)

# Get metrics from /proc
with open("/proc/loadavg") as out:
    output = out.read()
loadavg = output.splitlines()

with open("/proc/meminfo") as out:
    output = out.read()
meminfo = output.splitlines()

with open("/proc/swaps") as out:
    output = out.read()
swaps = output.splitlines()

with open("/proc/uptime") as out:
    output = out.read()
uptime = output.splitlines()

# Build metrics dictionary
metrics_out = {
    "TimeStamp": time.time(),
    "LoadAvg": loadavg,
    "MemInfo": meminfo,
    "Swaps": swaps,
    "UpTime": uptime
}

# Write log file
with open(logfilename, "w") as logfile:
    json.dump(metrics_out, logfile)
