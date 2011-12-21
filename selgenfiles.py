#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# バッチファイル書くところを変更するとWin以外でもおｋ？
# 
# 必要なものを取ってきて、適当に使えるようにする
# 
#   ・Python 2.x
#   ・DocUtils
#   ・BeautifulSoup
#   ・Selenium
# 
# 
# <試行手順>
#
# 1.reST書く (testcase.rst)
# 
# 2.reSTを HTML にする
# 
#   > rst2html testcase.rst testcase.html
# 
# 3.このスクリプトを実行する
# 
# 4．ファイルが出来てる。
# 
# 5. 生成された .batファイルを実行
# 

from BeautifulSoup import BeautifulSoup
from xml.sax.saxutils import *
import re
import os

p= re.compile(r'\&\#(\d*)\;')

# p= re.compile(r'\&\#(\d*)\;')
def cnv10646( match ):
    n = int(match.groups(0)[0])
    try:
        s = unichr(n).encode('utf-8')
    except:
        s= '?'
    return s

def gentestsuite( file ):

    f = open(file)

    #     
    buf=''
    for x in f:
        buf = buf + x

    cont = BeautifulSoup(buf)


    st =  cont.findAll('table')

    suitetitle =''
    suitelist = []
    caselist = []
    parmdict = {}

    for x in st:

        tblclass = x['class']

        steps = []

        # paramater list
        if 'field-list' in tblclass:
            col =  x.findAll('col')
            if len(col) == 2:
                tr = x.findAll('tr')
                title =''
                list =[]
                for y in tr:
                   th =  y.find('th')
                   td =  y.find('td')

                   parmdict[th.text.rstrip(':')] =  td.text
                   


        # suite list
        elif 'suitelist' in tblclass:
            col =  x.findAll('col')
            if len(col) == 1:

                suitetitle = x.find('th').text

                td = x.findAll('td')

                for y in td:
                    suitelist.append(y.text)

        # case list
        elif 'testcase' in tblclass:
            col =  x.findAll('col')
            if len(col) == 3:

                th = x.find('th')
                tr = x.findAll('tr')
                c = 0

                steps = []
                for y in tr:
                    td = y.findAll('td')

                    buf = []
                    for z in td:
                        buf.append(p.sub(cnv10646,unescape(z.text)).replace(r'&nbsp;',' ').rstrip())
                    if len(buf) > 0:
                        steps.append(buf)

                if len(steps) > 0 :
                    caselist.append((th.text,steps))

        else:
            none

    fsuite = open(suitetitle+'.html','w')

    print >>fsuite, '<html><head><title>'+suitetitle+'</title></head><body>'
    print >>fsuite, '<h1>'+suitetitle+'</h1>'
    print >>fsuite, ''

    print >>fsuite, '<table cellpadding="1" cellspacing="1" border="1">'
    print >>fsuite, '<tr><td>'+suitetitle+'</td></tr>'

    for x in range(len(suitelist)):
        print suitelist[x]

        print >>fsuite,r'<tr><td><a href="'+suitelist[x]+'.html">'+suitelist[x]+'</a></td></tr>'

        (v,w) = caselist[x]

        if suitelist[x] == v:
            fcase = open(v+'.html','w')

            print >>fcase,r'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">'
            print >>fcase,r'<html>'
            print >>fcase,r'<head>'
            print >>fcase,r'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
            print >>fcase,r'<title>'+ v +'</title></head><body>'
            print >>fcase,''

            print >>fcase,'<table cellpadding="1" cellspacing="1" border="1">'
            print >>fcase,'<thead>'
            print >>fcase,'<tr><td rowspan="1" colspan="3">'+v+'</td></tr>'
            print >>fcase,'</thead><tbody>'

            for y in w:
                print >>fcase,'<tr>'
                for x in y:
                   print >>fcase,'   <td>'+x+'</td>'
                print >>fcase,'</tr>'
            print >>fcase, '</tbody></table></body></html>'

            fcase.close


    print >>fsuite, '</table></body></html>'

    fsuite.close()

    # bat file

    fcmdline = open( parmdict['BAT'],'w' )

    print >>fcmdline,r'java -jar %s -htmlSuite "*%s" "%s" "%s" "%s" -timeout "%s"' % \
          ( parmdict['SELENIUM'] ,
            parmdict['BROWSER'] ,
            parmdict['TESTDOMAIN'] ,
            parmdict['SERVERDIR'] +'\\'+parmdict['TESTSUITE'] ,
            parmdict['SERVERDIR'] +'\\'+parmdict['RESULTFILE'] ,
            parmdict['TIMEOUT'] )

    fcmdline.close()

if __name__ == '__main__':

    gentestsuite('testcase.html')
