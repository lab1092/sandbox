# potsv2rst.py 
# 
# usage:
#  1. run podiffreport.py -> result.tsv
#  2. run potsv2rst.py
#
# copy following 2 lines C:\Python26\Lib\site-packages\sitecustomize.py
#  
#  import sys
#  sys.setdefaultencoding("utf-8")
#

infilename = "result.tsv"
outfilename = "index.rst"


flg=0

key = u""
note = u""
buf = []

fi = open(infilename)
foo = open(outfilename,"w")

print >> foo , "Welcome to podiff's documentation!"
print >> foo , "=================================="
print >> foo , ""
print >> foo , "Contents:"
print >> foo , ""
print >> foo , ".. toctree::"
print >> foo , "   :maxdepth: 1"
print >> foo , ""

def filerst(msg,cnt):

    outfilename = str(cnt).zfill(6) + ".rst"


    fo = open(outfilename,"w")

    print >> fo, "==========================="
    print >> fo, str(cnt) + "からー"
    print >> fo, "==========================="
    print >> fo, ""
    print >> fo, ""
    print >> fo, msg
   
    fo.close()

    print >> foo , "   " + str(cnt).zfill(6)

#----------------

def writetorst(flag,num,linenum,msgid,msgstr,fuzzy):

    buf = []

    
    buf.append(num)
    buf.append('-----------------')
    buf.append('')

    s = ""
    if flag == "+":
        s = "[+] "

    if fuzzy != "":
        s = s + "fuzzy"

    buf.append(s)
    buf.append('')

    buf.append( '.. _L'+ num.zfill(6) +'-label:\n')
    
    buf.append('   ::\n')

    if msgid == "":
        msgid = "[Enpty]"

    buf.append('      '+ msgid)
    buf.append('')
    buf.append('   ::\n')

    if msgstr == "":
        msgstr = "[Enpty]"

    buf.append('      '+ msgstr)

    msg = '\n' + '\n'.join(buf) + '\n'

    return msg

#---------------

lnum = 1        # linenumber
mcnt = 0        # message count (= pootleid???)
podict = {}
curtag = ""
flg =0

pagelen = 1000
pagecnt = 0

c = 1

msg = ""

for line in fi:

    line = line.rstrip('\n')
    (flag,num,linenum,msgid,msgstr,fuzzy) = line.split('\t')

    msg = msg + writetorst(flag,num,linenum,msgid,msgstr,fuzzy)
    
    mcnt = mcnt +1
    
    if (mcnt % pagelen ) == 0 and msg != "":
        filerst(msg,pagecnt)
        pagecnt = pagecnt +pagelen
        msg = ""

    lnum = lnum +1


if mcnt > pagecnt :
    filerst(msg,pagecnt)
    print pagecnt

print >> foo , ""
print >> foo , "Contents-II:"
print >> foo , ""
print >> foo , ".. toctree::"
print >> foo , "   :maxdepth: 1"
print >> foo , ""
print >> foo , "   translation_memo"
print >> foo , ""
print >> foo , "Indices and tables"
print >> foo , "=================="
print >> foo , ""
print >> foo , "* :ref:`genindex`"
print >> foo , "* :ref:`search`"


