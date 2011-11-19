# -*- coding: utf-8 -*-
#
# run Windows Help Compiler
# (copy this file to sphinx project folder)

import os
import sys
import conf

# modify the path for your own environment
runpath = r'C:\Program Files\HTML Help Workshop'
exepath = runpath + '\\' + 'hhc.exe'

# htmlfile folder
htmpath = '_build\\htmlhelp\\' 

# .hhp
cnffile = htmpath+conf.htmlhelp_basename + '.hhp'

# .chm
chmfile = htmpath+conf.htmlhelp_basename + '.chm'

cmdline = ('"%s" %s' )% (exepath,cnffile)

os.popen(cmdline,'r')
sys.stdout.flush()

os.popen(chmfile,'r')
sys.stdout.flush()
