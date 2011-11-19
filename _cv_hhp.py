# -*- coding: utf-8 -*-
#
# 文字変換するよ(設定ファイル)
#

import os
import sys
import conf

# .hhp
cvpath = '_build\\htmlhelp\\'+conf.htmlhelp_basename + '.hhp'

fi = open(cvpath,'r')

buf = []
while 1:
    line = fi.readline()

    if not line:
        break

    if 'Default Font=' in line:
        buf.append('Default Font=MS UI Gothic,8,128')
    elif 'Language=' in line:
        buf.append('Language=0x411')
    else:
        buf.append(line)

fi.close()

#

fo = open(cvpath,'w')

for x in buf:
    fo.write(x)

fo.close()


