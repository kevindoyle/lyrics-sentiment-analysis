# Collects URLS

import urllib2
import sys
import re
import time

def get_urls( url, name ):
   base = "http://www.azlyrics.com/"

   print url, name
   
   source = urllib2.urlopen("{0}{1}".format( base, url )).read()

   print len(source)

   pattern = re.compile(r'\.\./lyrics/' + name + '/(?:.*?)\.html')

   #print pattern

   test_string = "../lyrics/" + name + "/dreams07.html"

   test_url = re.findall( pattern, test_string )

   print "test: ", len(test_url)

   urls = re.findall( pattern, source )

   print len(urls)

   with open("{0}URL.txt".format(name), 'w+') as f:
      for address in urls:
         f.write( base + address[3:] + '\n' )
      
if __name__ == '__main__':
   
   list_file = sys.argv[1]
   
   with open(list_file, 'r') as arts:
      art_list = arts.readlines()
      
      i = 0
      
      while i < len( art_list ):
         url = art_list[i].strip()
         name = art_list[i+1].strip()
         get_urls( url, name )
         time.sleep(10) 
         i = i+2