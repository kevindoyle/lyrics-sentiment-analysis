Last updated: 2015/5/29

Welcome! This is a quick, fun project I work on occasionally. It's not very well structured. Please don't judge me :)

Attention:
If you're downloading this hoping to use it as is, it's not going to work.
-You need some libraries, listed below. These are not difficult to get.
-You need a sentiment analysis tool. This will probably be a problem. Sorry.

Non-standard Libraries used:
   NLTK
   scikit-learn
   newspaper

What I have in .git/info/exclude:
   *.pyc
   *.dic
   word_category_counter.py
   *EXT.txt

Steps to take to do this:

!!!!
!!!!
!!!!1

Manually collect the artist names and the root for the
artists' song lyric URLs. 

They go into a file formatted :

   URLbase
   name
   
real example:

   n/nickiminaj.html
   nickiminaj
   
@@@@
@@@@
@@@@2

Run url_get.py

   python url_get.py <name of file made in step 1>
   
This creates a bunch of files called <artist name>URL.txt
Each file contains a list of URLs for every song from that artist.

####
####
####
####3

Run lyric_grab.py

   python lyric_grab.py <name of file made in step 1>
   
This creates a bunch of files called <artist name>EXT.txt
Each file contains all of the extracted text from each artist's URL list.

Note: This will take a long time to run. Estimate: 21 seconds per lyric URL.
      It takes a long time, but avoids getting banned. 
      
$$$$
$$$$
$$$$
$$$$4

Run liwc_processing.py

   python liwc_processing.py <name of file made in step 1>

This creates a bunch of files called <artist name>SCORES.txt 
   and files called <artist name>SCORES.pickle
Only the pickle files are actually used. Both contain LIWC scores for the given artist.

%%%%
%%%%
%%%%
%%%%5

Run clustering.py

   python clustering.py <name of file made in step 1>
   
This file is still in progress. 
It prints out the comparison evaluation for an artist hard coded in line 66
