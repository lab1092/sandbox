# -*- coding: utf-8 -*-
#
# 文字変換するよ(index)
#  "_build/htmlhelp/remedyhelpdoc.hhc"が生成されていること

import os
import sys
import re

import conf

# .hhk
cvpath = '_build\\htmlhelp\\'+conf.htmlhelp_basename + '.hhc'

# def
def foo(match):
    n = int(match.groups(0)[0])
    try:
        s = unichr(n).encode('mbcs')
    except:
        s= "?"
    return s


#
p= re.compile(r'\&\#(\d*)\;')

fi = open(cvpath,'r')

buf = []
while 1:
    line = fi.readline()

    if not line:
        break

    buf.append(p.sub(foo,line))

fi.close()

#

fo = open(cvpath,'w')

for x in buf:
    fo.write(x)

fo.close()


