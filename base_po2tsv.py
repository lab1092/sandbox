# base_po2tsv.py 
# 
# usage:
#  1. copy this file and ja.po on same directory.
#  2. python po2tsv.py
#
# copy following 2 lines C:\Python26\Lib\site-packages\sitecustomize.py
#  
#  import sys
#  sys.setdefaultencoding("utf-8")
#

infilename = "ja.po"
outfilename = "ja.tsv"

linetags = ( "msgid","msgstr" )

flg=0

key = u""
note = u""
buf = []

fi = open(infilename)
fo = open(outfilename,"w")


#----------------

def writetotsv(podict,tags,key,mcnt,fuzzyflg):

    buf = []
    
    buf.append(str(mcnt))

    if podict.has_key(key):
       buf.append( 'L'+ str(podict[key]).zfill(6) )
    else:
       buf.append('<None>')
       
    for tag in tags:
        if podict.has_key(tag):
            buf.append('_\\a_ '.join(podict[tag]) )
        else:
            buf.append('<None>')

    if fuzzyflg == 'f':
        buf.append('Fuzzy')
    else:
        buf.append('')

    msg = '\t'.join(buf)

    print >> fo,msg

#---------------

lnum = 1        # linenumber
mcnt = 0        # message count (= pootleid???)
podict = {}
curtag = ""
flg =0
fuzzyflg = None # fuzzy

for line in fi:

    if line.strip() == '':
        
        if podict.has_key('lnum'):
            writetotsv(podict,('msgid','msgstr'),'lnum',mcnt,fuzzyflg)
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
    writetotsv(podict,('msgid','msgstr'),'lnum',mcnt,fuzzyflg)


fi.close()
