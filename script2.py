import glob # This is a built-in python package
import sys
import topic
searcher = topic.Searcher()
for filename in searcher.search('algorithm', 2, glob.glob('*.txt')):
	print(filename)

