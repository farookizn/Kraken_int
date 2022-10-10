# To find the number of Ip's from log file and list in descending order.
# Author - Farook
# Date - 01/10/2022

import re
import operator

def countIp(logfile):
    openFile = open(logfile, "r").readlines()

    wordfreq = {}

    for line in openFile:
        ipAddr = line.split(" ")[1]
        if ipAddr not in wordfreq:
            wordfreq[ipAddr] = 0

        wordfreq[ipAddr] += 1

    # sorting the dict
    sorted_ips = dict(sorted(wordfreq.items(), key=operator.itemgetter(1), reverse=True))

    for ipAddr, count in sorted_ips.items():
        print("{} {}".format(count, ipAddr))

countIp("Sys_out.log")