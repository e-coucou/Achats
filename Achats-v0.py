# -*- coding: utf-8 -*-
#---------------------------------------
import sys
import os
import json
import csv
from os.path import join, getsize
#---------------------------------------
class ARBO:
    def __init__(self, marche=None,segment=None,fournisseur=None,montantHT=0):
        self.marche = marche
        self.segment = segment
        self.fournisseur = fournisseur
        self.montantHT = montantHT
#---------------------------------------
arb=[]
marche=[]
segment=[]
#---
def isMarche(m):
    for mar in marche:
        if (m==mar):
            return 0
    marche.append(m)
    return 0
#---
def isSegment(s):
    for seg in segment:
        if (s==seg):
            return 0
    segment.append(s)
    return 0
#---------------------------------------
cr = csv.reader(open("CA2013-4.csv","rb"))
for row in cr:
    #    print row
    arb.append(ARBO(row[0],row[1],row[2].lower(),row[3].rsplit(',')[0]))
    isMarche(row[0])
    isSegment(row[1])
#print json.dumps(arb,separators=(',',':'))
print '{"name":"Achats Industriels","children":['
flag_m1=1
for m in marche:
    flag_m = 1
    flag_s1 = 1
    for s in segment:
        flag_s = 1
        flag_i = 1
        for info in arb:
            if (info.marche==m) & (info.segment==s):
                if flag_m:
                    if flag_m1:
                        print '{"name":"%s",'%(m)
                        print '"children":['
                        flag_m1=0
                    else:
                        print '       ]}'
                        print ']},{"name":"%s",'%(m)
                        print '"children":['
                flag_m = 0
                if flag_s:
                    if flag_s1:
                        print '       {"name":"%s",'%(s)
                        print '       "children":['
                        flag_s1=0
                    else:
                        print '             ]},'
                        print '       {"name":"%s",'%(s)
                        print '       "children":['
                flag_s = 0
                if flag_i:
                    print '              {"name":"%s","size":%s}'%(info.fournisseur,info.montantHT)
                else:
                    print '              ,{"name":"%s","size":%s}'%(info.fournisseur,info.montantHT)
                flag_i = 0
print '       ]}'
print ']}'
print ']}'
fn=open('test.json','w')
#rep = '/Users/Eric/Documents/perso/Test'
#print listdir(rep)
#print json.dumps(toto(rep),separators=(',',':'))
fn.close()
