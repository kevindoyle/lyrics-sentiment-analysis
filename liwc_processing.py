import nltk
from nltk.collocations import *
import time
import re
import word_category_counter
import sys
import pickle

def process_lyrics( artist_name ):

   filename = artist_name + "EXT.txt"
   with open(filename, 'r') as f:
      raw_songs = f.read()

   print "Processing: ", filename
   # Taking the title and credits out of the file
   # Title
   pat1 = re.compile(r'(.+?LYRICS)')
   head = pat1.search(raw_songs).expand(r'\1')

   pat2 = re.compile(r'(".+?")')
   match2 = pat2.search(head).expand(r'\1')
   
   extraneous_crap = head[len(match2):]
   
   clean_raw_songs = raw_songs.replace(extraneous_crap, '')
   
   # Credits
   pattern = re.compile(r'(Visit www\.azlyrics.*?Search)')
   credits = re.findall(pattern, raw_songs)
   
   for credit in credits:
      clean_raw_songs = clean_raw_songs.replace(credit, ' ')
   
   raw_songs = clean_raw_songs
      
   # New line characters were mistakenly removed in the scraping process,
   # but they were replaced with ' ' and there were two of them, so here 
   # we can use '  ' to split the lines, instead of .splitlines()
   raw_lines = raw_songs.split('  ')
   song_sents = [nltk.word_tokenize(line) for line in raw_lines]
   song_words = [word.lower() for sent in song_sents for word in sent]


   words = []
   stops = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
               'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
               'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
               'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
               'what', 'which', 'who', 'whom', 'this', 'that', 'these', 
               'those', 'am', 'is', 'are', 'were', 'be', 'been',
               'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
               'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because',
               'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
               'about', 'between', 'into', 'through', 'during', 'before', 
               'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in',
               'out', 'on', 'over', 'under', 'further', 'then', 'once', 'here', 
               'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
               'each', 'few', 'other', 'some', 'such', 'only', 'own', 'same',
               'so', 'than', 'too', 'very', 's', 'can', 'will', 'just',
               'now', 'went', 'asked', 'was'] 
      
   words = song_words
   #for word in song_words:
   #   if len(re.findall(r'\w', word)) > 0:
   #      if word not in stops:
   #         words.append(word)


   #fdist = nltk.FreqDist(words)
   #print fdist.B()
   #print fdist.N()
   #print fdist.items()[:20], "\n\n"

   #bigram_measures = nltk.collocations.BigramAssocMeasures()
   #finder = BigramCollocationFinder.from_words(words)
   #finder.apply_freq_filter(3)
   #print finder.nbest(bigram_measures.pmi, 10), "\n\n"
   #print finder.ngram_fd.viewitems(), "\n\n"


   #bigrams = nltk.bigrams(words)
   #bfdist = nltk.FreqDist(bigrams)
   #print bfdist.items()[:20], "\n\n"

   liwc_scores = word_category_counter.score_text(raw_songs)
   normalized_liwc_scores = word_category_counter.normalize_scores(liwc_scores)
   
   outfile = "SCORES/" + artist_name + "SCORES.txt"
   with open(outfile, 'w') as outf:
      for name, value in normalized_liwc_scores.items():
         outf.write("{0}\n{1}\n".format(name, value))
   
   outfile = "SCORES/" + artist_name + "SCORES.pickle"
   with open(outfile, 'w') as outf:
      pickle.dump(normalized_liwc_scores, outf)

if __name__ == '__main__':
   list_file = sys.argv[1]
   art_list = None
   
   with open(list_file, 'r') as arts:
      art_list = arts.readlines()
      
   i = 0
   
   while i < len( art_list ):
      artist_name = art_list[i+1].strip()
      process_lyrics( artist_name )
      i = i+2
   