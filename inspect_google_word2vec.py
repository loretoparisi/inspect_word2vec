# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:39:34 2016

@author: Chris
@lastauthor: Loreto Parisi (loretoparisi at gmail dot com)
"""

import sys

# Explore Google's huge Word2Vec model.

import gensim
import logging

if len(sys.argv) <= 2:
        text="\nUsage: python %s MODEL VOCABULARY" % (sys.argv[0])
	text = text + "\nMODEL\t\tThe language model as binary format i.e. GoogleNews-vectors-negative300.bin"
	text = text + "\nVOCABULARY\t\tThe vocabulary folder path i.e. ./vocabulary"

	print text
        exit();


# Logging code taken from http://rare-technologies.com/word2vec-tutorial/
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load Google's pre-trained Word2Vec model.
datasetpath = sys.argv[1]
vocabularypath = sys.argv[2]

model = gensim.models.Word2Vec.load_word2vec_format(datasetpath, binary=True)  



# Does the model include stop words?
print("Does it include the stop words like \'a\', \'and\', \'the\'? %d %d %d" % ('a' in model.vocab, 'and' in model.vocab, 'the' in model.vocab))



# Retrieve the entire list of "words" from the Google Word2Vec model.
vocab = model.vocab.keys()

fileNum = 1

wordsInVocab = len(vocab)
wordsPerFile = int(100E3)

# Write out the words in 100k chunks.
for wordIndex in range(0, wordsInVocab, wordsPerFile):
    # Write out the chunk to a numbered text file.    
    with open(vocabularypath+"/vocabulary_%.2d.txt" % fileNum, 'w') as f:
        # For each word in the current chunk...        
        for i in range(wordIndex, wordIndex + wordsPerFile):
            # Write it out and escape any unicode characters.            
            f.write(vocab[i].encode('UTF-8') + '\n')
    
    fileNum += 1
