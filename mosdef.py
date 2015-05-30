import nltk
from nltk.collocations import *
import time
import re
import word_category_counter
from boilerpipe.extract import Extractor

#f = open('mosdefURL.txt', 'r')
#raw_url = f.read()
#f.close()

#URL_list = raw_url.splitlines()

#extractions = []
#for URL in URL_list:
#   extractions.append(Extractor(extractor='ArticleExtractor', url=URL))
#   print("Pulled {0}".format(URL))
#   time.sleep(10)  

f = open('extractions.txt', 'r')
raw_songs = f.read()
f.close()

raw_lines = raw_songs.splitlines()
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
   
for word in song_words:
   if len(re.findall(r'\w', word)) > 0:
      if word not in stops:
         words.append(word)


fdist = nltk.FreqDist(words)
#print fdist.B()
#print fdist.N()
#print fdist.items()[:20], "\n\n"

#bigram_measures = nltk.collocations.BigramAssocMeasures()
#finder = BigramCollocationFinder.from_words(words)
#finder.apply_freq_filter(3)
#print finder.nbest(bigram_measures.pmi, 10), "\n\n"
#print finder.ngram_fd.viewitems(), "\n\n"

bigrams = nltk.bigrams(words)
bfdist = nltk.FreqDist(bigrams)
#print bfdist.items()[:20], "\n\n"

liwc_scores = word_category_counter.score_text(raw_songs)

for name, value in liwc_scores.items():
   print name, value
"""   
print "Neg", liwc_scores["Negative Emotion"], "\n"
print "Pos", liwc_scores["Positive Emotion"], "\n"
print "Anger", liwc_scores["Anger"], "\n"
print "Death", liwc_scores["Death"], "\n"

print "Friends", liwc_scores["Friends"], "\n"
print "Family", liwc_scores["Family"], "\n"
print "Swear Words", liwc_scores["Swear Words"], "\n"

print "Adverbs", liwc_scores["Adverbs"], "\n"
print "Fillers", liwc_scores["Fillers"], "\n"

print "Achievement", liwc_scores["Achievement"], "\n"
print "Money", liwc_scores["Money"], "\n"
print "Work", liwc_scores["Work"], "\n"

print "Sexual", liwc_scores["Sexual"], "\n"
print "Feel", liwc_scores["Feel"], "\n"

print "Exclusive", liwc_scores["Exclusive"], "\n"
print "Inclusive", liwc_scores["Inclusive"], "\n"
"""
   
"""
song_toks = []

for song in extractions:
   num = song.getText().count('\n')
   song_sent = song.getText().splitlines( num )
   song_words = [nltk.word_tokenize(sent) for sent in song_sent]
   song_toks.append(song_words)

   
f = open('extractions.txt', 'w')

for song in song_toks:
   for sent in song:
      for word in sent:
         try:
            f.write(word)
            f.write(" ")
         except UnicodeEncodeError:
            print "Error word\n"
            f.write("ERROR")
            f.write(" ")
      f.write("\n")
   f.write("\n\n")
   
f.close()

print song_toks[0]
print "Done!"
"""

   