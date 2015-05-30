# Processing the scores and creating clusters

import sys
import pickle
from sklearn.cluster import KMeans


if __name__ == '__main__':
   list_file = sys.argv[1]
   artist_name_dic = {}
   
   with open(list_file, 'r') as arts:
      art_list = arts.readlines()
      
   i = 0
   
   # Will be a dictionary of dictionaries
   # Keys are artist names, then LIWC categories
   scores_dic = {}
   
   while i < len( art_list ):
      artist_name = art_list[i+1].strip()
      artist_name_dic[artist_name] = 0
      score_file_name = artist_name + "SCORES.pickle"
      with open(score_file_name, 'r') as sfn:
         scores = pickle.load(sfn)
      scores_dic[artist_name] = scores
      i = i+2
   
   
   # Artist scores grouped by LIWC category
   # Keys are LIWC categories, then artist names
   grouped_scores = {}
   for sent_key in scores_dic['nickiminaj'].keys():
      grouped_scores[sent_key] = {}
      for name_key in scores_dic.keys():
         grouped_scores[sent_key][name_key] = scores_dic[name_key][sent_key]
         
   # Keys are LIWC categories, then numbers for the groups
   clusters = {}
   for key in grouped_scores.keys():
      clusters[key] = {}
      names = [ [name] for name,number in grouped_scores[key].items() ]
      numbers = [ [number] for name,number in grouped_scores[key].items() ]
      #score_pairs = [ values for values in grouped_scores[key].items() ]
      #print key, '\n', sorted(score_pairs, key=lambda pairs: pairs[1])
      #for num in xrange(1,5):
      kmean = KMeans(n_clusters = 7)
      kfit = kmean.fit(numbers)
      for idx,grp in enumerate(kfit.labels_):
         try:
            clusters[key][grp] += names[idx]
         except KeyError:
            clusters[key][grp] = names[idx]
   
   """  #FOR OUTPUT OF ALL CLUSTERS
   for key in clusters.keys():
      print key
      for group in clusters[key].items():
         print group
      print '\n\n'
   """
   artist_name_dic['NONE'] = 0
   for key in open("cats_selection.txt", 'r').read().splitlines():
      for group in clusters[key].items():
         if 'taylorswift' in group[1]:
            if len(group[1]) == 1:
               artist_name_dic['NONE'] += 1
            for name in group[1]:
               artist_name_dic[name] += 1
               
               
   results = artist_name_dic.items()
   results = sorted( results, key=lambda pairs: pairs[1], reverse=True)
   print results[1][0], " is most like ", results[0][0]
   #print results
   
   print results
   