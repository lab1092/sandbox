#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Seleniumの実行結果ファイルをもとに
# reSTを作ってみよう的試み。
# とりあえず版。
#
# Seleniumの結果HTMLを与えると、reST形式のファイルを生成します。
# (result.html -> result.rst)
#

from BeautifulSoup import BeautifulSoup
import os
import os.path

def resulthtmltorst( file ):

    f = open(file)

    #     
    buf=''
    for x in f:
        buf = buf + x

    cont = BeautifulSoup(buf)

    frest = open( os.path.splitext(file)[0] + '.rst','w')

    h1 = cont.find('h1')
    
    #header
    
    print >>frest,h1.text
    print >>frest,'======================================================'
    print >>frest,''
    print >>frest,'   :generated: resulthtmltorst.py'
    print >>frest,'   :filename:',file
    print >>frest,''
    print >>frest,'**Test Results**'

    # pick up every result from html tables
    # [0]:Result summary + CaseList
    # [1]:CaseList
    # [2]:Case Results
    # [3]:Case Result...
    #  :

    rs = cont.findAll('table')
    
    c = 0
    
    for x in rs:
        print >>frest,''
        
        # Result summary 
        if c == 0:

            print >>frest,'.. list-table::'
            print >>frest,''
            tr = x.findAll('tr')

            for y in tr:
            
                td = y.findAll('td')
                
                if len(td) != 2:
                    break
                    
                v = td[0].text.replace(':','')
                w = td[1].text
                
                print >>frest,'   * - ',v
                print >>frest,'     - ',w
                
                
            h1 = x.find('h1')
            
            print >>frest,''
            print >>frest,h1.text
            print >>frest,'-----------------------------------------'

            
        # CaseList
        elif c == 1:
            
            tr = x.findAll('tr')

            f = 0
            for y in tr:
                if f == 0 and 'title' in y['class']:

                    td = y.find('td')
                    print >>frest,''
                    print >>frest,td.text
                    print >>frest,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                    print >>frest,''
                    print >>frest,'**'+y['class'].split(' ')[1]+'**'
                    print >>frest,''
                    print >>frest,'.. list-table::'
                    print >>frest,''

                    f = 1
                else:

                    td = y.findAll('td')
                    print >>frest,'   * - ' , td[0].text
                    if y.has_key('class'):
                        print >>frest,'     - ' , y['class'].strip()
                    else:
                        print >>frest,'     - (None)'


        
        # Case Results
        elif c == 2:
            None
            
        
        # Case Result
        else:

            tr = x.findAll('tr')

            f = 0
            for y in tr:
                if f == 0 and 'title' in y['class']:


                    
                    td = y.find('td')
                    print >>frest,''
                    print >>frest,td.text+'.html'
                    print >>frest,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                    print >>frest,''
                    print >>frest,'**'+y['class'].split(' ')[1]+'**'
                    print >>frest,''
                    print >>frest,'.. list-table::'
                    print >>frest,''

                    f = 1
                else:

                    td = y.findAll('td')
                    print >>frest,'   * - ' , td[0].text
                    print >>frest,'     - ' , td[1].text
                    print >>frest,'     - ' , td[2].text
                    if y.has_key('class'):
                        print >>frest,'     - ' , y['class'].strip()
                    else:
                        print >>frest,'     - (None)'



        c = c+1

  
    
    rs = cont.findAll('pre')

    print >>frest,''
    print >>frest,'Info'
    print >>frest,'----'
    print >>frest,''

    p =  str(rs[0])
    q = p.split('\n')

    

    # 1st table:Summary
    rs = cont.findAll('table')



    # information
    rp = cont.findAll('pre')
    
    for x in rp:

        print >>frest,'::\n'

        y = str(x.renderContents()).split('\n')
        for z in y:
            print >>frest,'   ' + z
    
    frest.close()

if __name__ == '__main__':

    resulthtmltorst('result.html')
