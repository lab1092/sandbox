# podiffreport.py 
# 
# usage:
#  1. copy this file and ja-base-20110731_249bmerge.tsv on same directory.
#  2. generate ja-base-20110731.tsv from ja-base-20110731.po by using "base_po2tsv.py"
#  2. python diff2tsv.py
#
# copy following 2 lines C:\Python26\Lib\site-packages\sitecustomize.py
#  
#  import sys
#  sys.setdefaultencoding("utf-8")
#

def makepodiff(defpolist,refpolist):

    buf = []
    c2 = []
    f1 = []
    f2 = []
    d2 = {}

    for (e1,e2,e3,e4,e5) in defpolist:
            f1.append(0)

    for (e1,e2,e3,e4,e5) in refpolist:

        if e3 != "":
            c2.append((e1,e2,e3,e4,e5))
            d2[e3] = (e1,e2,e3,e4,e5)
            f2.append(0)
        else:
            f2.append(0)

    # append 
    
    
    
    
    
    for (ee1,ee2,ee3,ee4,ee5) in defpolist:
    
        if d2.has_key(ee3):
            (e1,e2,e3,e4,e5) = d2[ee3]
            buf.append(('=',ee1,ee2,ee3,ee4.rstrip(),ee5,e1,e2,e3,e4.rstrip(),e5))
    
            f1[int(ee1)-1]=1
            f2[int(e1)-1]=1
        else:        
            buf.append(('+',ee1,ee2,ee3,ee4.rstrip(),ee5,'','','',''))
            

    
    c = 0
    for x in f2:
        if f2[c] == 0 and c < len(c2) :
            (e1,e2,e3,e4,e5) = c2[c]
            buf.append(('-','','','','','',e1,e2,e3,e4.rstrip(),e5))
    
        c = c +1



    return buf

def generateline(podict,tags,key,mcnt,fuzzyflg):

    buf = []
    
    buf.append(str(mcnt))

    if podict.has_key(key):
       buf.append( 'L'+ str(podict[key]).zfill(6) )
    else:
       buf.append('<None>')
       
    for tag in tags:
        if podict.has_key(tag):
            buf.append(''.join(podict[tag]) )
        else:
            buf.append('<None>')

    if fuzzyflg == 'f':
        buf.append('fuzzy')
    else:
        buf.append('')

    return buf

#---------------

def readpofile(name):
    linetags = ( "msgid","msgstr")
    lnum = 1        # linenumber
    mcnt = 0        # message count (= pootleid???)
    podict = {}
    curtag = ""
    flg =0
    buf = []
    fuzzyflg = None # fuzzy
    
    
    fi = open(name)
    
    for line in fi:
    
        if line.strip() == '':
            
            if podict.has_key('lnum'):
                buf.append(generateline(podict,('msgid','msgstr'),'lnum',mcnt,fuzzyflg))
                mcnt = mcnt + 1
            
            podict = {}
            curtag = ''
            
            fuzzyflg = None
            
        else:
            flg =0
            
            # 
            if line.startswith('#,'):
                if 'fuzzy' in line:
                    fuzzyflg = 'f'
            
            for tag in linetags:
                if line.startswith(tag+' '):
                   if tag == 'msgid':
                      podict['lnum'] = lnum
                   s = line[len(tag):].strip().strip('\x22')
                   podict[tag] = [s]
                   curtag = tag
                   flg =1
                   break
            
            if curtag != '' and flg == 0:
                s = line.strip().strip('\x22')
                podict[curtag].append(s)
        
        lnum = lnum +1
    
    if podict.has_key('lnum'):
        buf.append(generateline(podict,('msgid','msgstr'),'lnum',mcnt,fuzzyflg))
    
    
    fi.close()

    return buf

#
def doreport(defpolist,refpolist,outtsv,outmode):

    tsvlist = []
    
    tsvlist = makepodiff(defpolist,refpolist)

    if len(defpolist) > 0 and len(refpolist):
        
        if outmode == "tsvwithmark":
            
            for x in tsvlist:
                print '\t'.join(x)
            
def podiffreport(defpo,refpo,outtsv,outmode):

    buf = []
    defpolist = []
    refpolist = []

    defpolist = readpofile(defpo)
        
    refpolist = readpofile(refpo)

    doreport(defpolist,refpolist,outtsv,outmode)


podiffreport("ja.po","ja_2012_0106.po","result.tsv","tsvwithmark")