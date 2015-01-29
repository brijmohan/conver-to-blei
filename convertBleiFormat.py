#!/usr/bin/env python
# encoding: utf-8

'''
	This file converts text corpora to blei format
	two params:
	python convertBleiFormat.py <folder with input text file> <output folder>
'''
import sys
import nltk
from os import listdir, makedirs
from os.path import isfile, join, exists

STOPWORDS = nltk.corpus.stopwords.words("english")
VOCAB = {}

def createVocab(inpdir, opdir):
	files = listdir(inpdir)
	vocab_cnt = 1
	for idx, f in enumerate(files):
		with open(join(inpdir, f)) as docfile:
			words = (docfile.read().decode('ascii', 'ignore')).strip().split()
			for w in words:
				w = w.lower()
				if w != '' and w not in STOPWORDS and w not in VOCAB:
					VOCAB[w] = vocab_cnt
					vocab_cnt += 1
	with open(join(opdir, 'vocab.txt'), 'wb') as vfile:
		for k, v in VOCAB.items():
			vfile.write(k + '\n')
			

def createXMLAndDat(foldername, opdir):
	op = open(join(opdir, 'data.txt'), 'wb')
	datFile = open(join(opdir, 'data.dat'), 'wb')
	files = listdir(foldername)
	for idx, f in enumerate(files):
		freq_table = {}
		op.write('<DOC>\n')
		op.write('<DOCNO>%d</DOCNO>\n' % idx)
		op.write('<TEXT>\n')
		with open(join(foldername, f)) as docfile:
			doctext = ' '.join((docfile.read().decode('ascii', 'ignore')).split('\n'))
			op.write(doctext + '\n')
			# find word associations
			words = doctext.split()
			for w in words:
				w = w.lower()
				if w != '' and w in VOCAB:
					w_id = VOCAB[w]
					if w_id in freq_table:
						freq_table[w_id] = freq_table[w_id] + 1
					else:
						freq_table[w_id] = 1
			
			datLine = str(len(freq_table))			
			for wid, f in freq_table.items():
				datLine += (' ' + str(wid) + ':' + str(f))
			datFile.write(datLine + '\n')
			
		op.write('</TEXT>\n')
		op.write('</DOC>\n')
	
	op.close()
	datFile.close()

if __name__ == '__main__':
	args = sys.argv
	inpdir = args[1]
	opdir = args[2]
	print args
	if not exists(opdir):
		makedirs(opdir)
	
	createVocab(inpdir, opdir)
	createXMLAndDat(inpdir, opdir)
