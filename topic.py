import sys
class Searcher:
	def search(instance, term, number, lis): #i dont feel this is how it was supposed to be done but it works (ie we were supposed to create an iterator but i completely ignore the instance and just do the same exact script as i did in part 1)
		lister = []
		for item in lis:
			count = open(item).read().count(term)	
			if int(count) >= int(number):
			    lister.append(item) 
				 
		return lister
