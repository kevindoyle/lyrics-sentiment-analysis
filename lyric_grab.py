import nltk
from nltk.collocations import *
import time
import sys
import re
import urllib2
from random import shuffle
import word_category_counter
from newspaper import Article, Config

USER_AGENTS = [ "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
              ]


def pick_time():
   times = [ 5, 6, 7, 8, 9, 10, 20, 30]
   shuffle(times)
   return times[0]

def mix_scrape_save( URL, name):
   outfile = name + "EXT.txt"
   text = ''
   
   shuffle(USER_AGENTS)
   
   try:
      #extractions.append(Extractor(extractor='ArticleExtractor', url=URL))
      #config = Config()
      #print USER_AGENTS[0]
      #config.browser_user_agent = USER_AGENTS[0]
      article = Article(URL, browser_user_agent = USER_AGENTS[0])
      article.download()
      article.parse()
      text = article.text.replace('\n', ' ')
      if len(text) > 0:
         print("Pulled {0}".format(URL.strip()))
      else:
         print("Error {0}".format(URL.strip()))
      time.sleep(pick_time())  
   except urllib2.HTTPError:
      print("HTTPError {0}".format(URL.strip()))
      time.sleep(8)
      
   with open(outfile, 'a') as of:
      for char in text:
         try:
            of.write(char)
         except UnicodeEncodeError:
            pass
   
   
def scrape_and_save( name ):
   infile = name + "URL.txt"
   outfile = "EXT/" + name + "EXT.txt"
   extractions = []

   with open(infile, 'r') as f:
      raw_url = f.read()
      f.close()

      URL_list = raw_url.splitlines()

      
      for URL in URL_list:
         try:
            #extractions.append(Extractor(extractor='ArticleExtractor', url=URL))
            article = Article(URL)
            article.download()
            article.parse()
            text = article.text.replace('\n', ' ')
            extractions.append(text)
            print("Pulled {0}".format(URL.strip()))
            time.sleep(pick_time())  
         except urllib2.HTTPError:
            print("HTTPError {0}".format(URL.strip()))
            time.sleep(8)
      
      
   with open(outfile, 'a') as of:
      for song in extractions:
         for char in song:
            try:
               of.write(char)
            except UnicodeEncodeError:
               pass
         
if __name__ == '__main__':
   list_file = sys.argv[1]
   
   with open(list_file, 'r') as arts:
      art_list = arts.readlines()
      
      i = 0
      """
      while i < len( art_list ):
         name = art_list[i+1].strip()
         scrape_and_save( name )
         time.sleep(10) 
         i = i+2
      """
      URL_name_list = []
      while i < len( art_list ):
         name = art_list[i+1].strip()
         URLfile = name + "URL.txt"
         
         with open(URLfile, 'r') as f:
            URL_list = f.readlines()
         
         for URL in URL_list:
            URL_name_list.append( (URL.strip(), name) )
         
         #time.sleep(10) 
         i = i+2
         
      print "URL_name_list: ", len(URL_name_list)
      
      shuffle(URL_name_list)
      
      for URL, name in URL_name_list:
         mix_scrape_save( URL, name )