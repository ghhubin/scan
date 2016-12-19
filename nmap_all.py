# -*- coding:utf-8 -*-
import datetime
import os

ips = '61.183.0.22-39'

CurTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = ips+'_'+CurTime
cmdstr = 'nmap -Pn -n -p- -vv -min-hostgroup 10 -min-parallelism 20 -oA '+ filename + ' ' + ips
os.system(cmdstr)

