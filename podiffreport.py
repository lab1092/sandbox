# podiffreport.py 
# 
# usage:
#  1. copy this file and ja-base-20110731_249bmerge.tsv on same directory.
#  2. generate ja-base-20110731.tsv from ja-base-20110731.po by using "base_po2tsv.py"
#  3. python podiffreport.py
#
# copy following 2 lines C:\Python26\Lib\site-packages\sitecustomize.py
#  
#  import sys
#  sys.setdefaultencoding("utf-8")
#

# generate pol diff list from two po
# in ( id , line num , msgid , msgstr )
#
# Flags:
#   '+' is new added , '-' is unused ,'=' is same entry
#
def makepodiff(defpolist,refpolist):

    buf = [] 
    c2 = []  
    f1 = []  # used flag list
    f2 = []  # used flag list
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

    # append entry
    
    for (ee1,ee2,ee3,ee4,ee5) in defpolist:
    
        # same
        if d2.has_key(ee3):
            (e1,e2,e3,e4,e5) = d2[ee3]
            buf.append(('=',ee1,ee2,ee3,ee4.rstrip(),
                        ee5,e1,e2,e3,e4.rstrip(),e5))
    
            f1[int(ee1)-1]=1
            f2[int(e1)-1]=1
        else:        

        # added
            buf.append(('+',ee1,ee2,ee3,ee4.rstrip(),ee5,
                        '','','','',''))
            

    
    c = 0
    for x in f2:
        if f2[c] == 0 and c < len(c2) :
        # not used
            (e1,e2,e3,e4,e5) = c2[c]
            buf.append(('-','','','','','',
                        e1,e2,e3,e4.rstrip(),e5))
    
        c = c +1



    return buf


# Generate line
#

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

# read the file and make po list
#

def readpofile(name):
    linetags = ( "msgid","msgstr")
    lnum = 1        # linenumber
    mcnt = 0        # message count (= pootleid???)
    podict = {}
    curtag = ""
    flg =0
    buf = []
    fuzzyflg = None # fuzzy
    
    #read the file    
    fi = open(name)
    
    for line in fi:
    
        # blank line is the trigger for store
        if line.strip() == '':
            
            if podict.has_key('lnum'):
                buf.append(generateline(podict,('msgid','msgstr'),
                                        'lnum',mcnt,fuzzyflg))
                mcnt = mcnt + 1
            
            podict = {}
            curtag = ''
            
            fuzzyflg = None
            
        
        else:
            flg =0
            
            # fuzzy mark( ad hoc )
            if line.startswith('#,'):
                if 'fuzzy' in line:
                    fuzzyflg = 'f'
            
            # messages with tag
            for tag in linetags:
                if line.startswith(tag+' '):
                   if tag == 'msgid':
                      podict['lnum'] = lnum
                   s = line[len(tag):].strip().strip('\x22')
                   podict[tag] = [s]
                   curtag = tag
                   flg =1
                   break
            
            # keep correct messages 
            if curtag != '' and flg == 0:
                s = line.strip().strip('\x22')
                podict[curtag].append(s)
        
        lnum = lnum +1
    
    # another trigger for stoer to list 
    if podict.has_key('lnum'):
        buf.append(generateline(podict,('msgid','msgstr'),
                                'lnum',mcnt,fuzzyflg))
    
    
    fi.close()

    return buf

# make report and write to file
#

def doreport(defpolist,refpolist,outname,outmode):

    difflist = []
    
    difflist = makepodiff(defpolist,refpolist)

    if len(defpolist) > 0 and len(refpolist):
        
        fo = open(outname,'w')
        if outmode == "tsvwithmark":
            
            for x in difflist:
                print >>fo,'\t'.join(x)
        
        elif outmode == "tsvdefonly":
        
            for x in difflist:
                print >>fo,'\t'.join(x[1:5])
            
        
        elif outmode == "tsvdefstrict":

            for x in difflist:
                buf = list(x[1:5])

                if x[0] == '-':
                    continue
                    
                if x[0] == '+':
                    buf[3]= ''
                print >>fo,'\t'.join(buf)

        else:

            # diff flag and poinfo
            for x in difflist:
                # added and existed 
                if x[0] == '+' or x[0] == '=':

                    print >>fo,'\t'.join(x[0:6])

                # '-' 
                else:

                    None


        fo.close()

# podiff 
#

def podiffreport(defpo,refpo,outtsv,outmode):

    buf = []
    defpolist = []
    refpolist = []

    defpolist = readpofile(defpo)
        
    refpolist = readpofile(refpo)

    doreport(defpolist,refpolist,outtsv,outmode)

podiffreport("ja.po","ja_2012_0106.po","result.tsv","")
