import re
import nltk
from collections import defaultdict

cent = open('cent_all.txt', 'r')
mosdef = open('mos_all.txt', 'r')
wutang = open('wu_all.txt', 'r')
nas = open('nas_all.txt', 'r')

cent_raw = cent.read()
wutang_raw = wutang.read()
mosdef_raw = mosdef.read()
nas_raw = nas.read()

cent_lines = cent_raw.splitlines()
wutang_lines = wutang_raw.splitlines()
mosdef_lines = mosdef_raw.splitlines()
nas_lines = nas_raw.splitlines()

print list

value_bank = defaultdict(list)

print value_bank

for cent, wu, mos, nas in zip(cent_lines, wutang_lines, mosdef_lines, nas_lines):
   cent_lab = ''.join(re.findall(r'^[a-zA-Z\s]*(?!\d)', cent))
   wu_lab = ''.join(re.findall(r'^[a-zA-Z\s]*(?!\d)', wu))
   mos_lab = ''.join(re.findall(r'^[a-zA-Z\s]*(?!\d)', mos))
   nas_lab = ''.join(re.findall(r'^[a-zA-Z\s]*(?!\d)', nas))
   
   
   if len(cent_lab) > 0:
      value_bank[cent_lab].append('cent: ' + ''.join(re.findall(r'\b[0-9.]*', cent)))
      value_bank[wu_lab].append('wu: ' + ''.join(re.findall(r'\b[0-9.]*', wu)))
      value_bank[mos_lab].append('mos: ' + ''.join(re.findall(r'\b[0-9.]*', mos)))
      value_bank[nas_lab].append('nas: ' + ''.join(re.findall(r'\b[0-9.]*', nas)))
      
      
   
for label in value_bank:
   max_val = max([float(num) for value in value_bank[label] for num in re.findall(r'\b[0-9.]*', value) if len(num) > 0])
   min_val = min([float(num) for value in value_bank[label] for num in re.findall(r'\b[0-9.]*', value) if len(num) > 0])

   if (max_val - min_val) > 1:
      print label
      for value in value_bank[label]:
         print '\t', value
   
   """
      print label
      print '  cent', '\t', ''.join(re.findall(r'\b[0-9.]*', cent))
      print '  wu', '\t', ''.join(re.findall(r'\b[0-9.]*', wu))
      print '  mos', '\t', ''.join(re.findall(r'\b[0-9.]*', mos))
      print '  nas', '\t', ''.join(re.findall(r'\b[0-9.]*', nas))
   else:
      print ''
   """
   
"""
for line in mosdef_lines:
   temp = re.findall(r'[0-9.]*', line)
   temp = ''.join(temp)
""" 
