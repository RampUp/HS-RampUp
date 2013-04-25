# Step 0. Load both text files
# Testing. Print out all the text
def readIn(filename):
	"""Takes in filename. Returns array of words in file"""
	with open(filename, 'r') as myfile:
		words = myfile.read().replace('\n', ' ').lower()
	return words.split()

def getCommonWords():
	"""Returns a list of common words"""
	fin = open('commonwords.txt', 'r')
	commons = [line.strip() for line in fin]
	commons = [word.lower() for word in commons]
	fin.close()
	return commons

oldwords = readIn("oldwords.txt")
newwords = readIn("newwords.txt")

# Step 1. Iterate through the text files
# Testing. Print out all the text

def printlist(lst):
	"""Neatly print out a list"""
	for word in lst:
		print word

printlist(oldwords + newwords)

# Step 2. Remove your name
# Testing. Print out "Removed! + word removed"

def removeName(lst, name):
	"""Remove name from list and return processed list"""
	ct = 0
	for word in lst:
		if name in word:
			lst.pop(ct)
			print "Removed! + " + word
		ct = ct + 1
	return lst


oldwords = removeName(oldwords, "Juliana")
newwords = removeName(newwords, "Juliana")

# Step 3. Remove punctuation
# Testing. Print our "Removed! + word removed"

def removePunctuation(lst):
	"""Removes all punctiation and returns processed list"""
	punctuation = ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', ':', ';']
	ct = 0
	for word in lst:
		for character in word:
			if character in punctuation:
				word = word.replace(character, "")
				lst[ct] = word
				print "Removed " + character + "from " + word
		ct = ct + 1
	return lst

oldwords = removePunctuation(oldwords)
newwords = removePunctuation(newwords)

# Step 3. Remove common words
# Testing. Print out "Removed! + word removed"

def removeCommonWords(lst):
	"""Removes all words in commons.txt from list and returns processed list"""
	commons = getCommonWords()
	parsedlst = []
	for word in lst:
		if word in commons:
			print "Removed common word: " + word
		if word not in commons:
			parsedlst.append(word)
	return parsedlst

oldwords = removeCommonWords(oldwords)
newwords = removeCommonWords(newwords)

# Step 4. Remove URLs
# Testing. Print out "Removed + url removed"

def removeURLs(lst):
	"""Removes all urls"""
	ct = 0
	for word in lst:
		if "http" in word:
			lst.pop(ct)
			print "Removed URL: " + word
		ct  = ct + 1

	return lst

oldwords = removeURLs(oldwords)
newwords = removeURLs(newwords)

# Step 5. Count how often each word appears
# Testing. Print out "Count + word"

def countUpWords(lst):
	"""Creates a freqency table for the number of times that a word appears"""
	wordcount = {}
	for word in lst:
		if word not in wordcount:
			wordcount[word] = 1
			print "Found new word: " + word
		else:
			wordcount[word] = wordcount[word] + 1
	return wordcount

oldwords_dict = countUpWords(oldwords)
newwords_dict = countUpWords(newwords)

# Step 6. Get top words
# Testing. Print out "Count + word"

def getTopWords(dictionary):
	"""Prints out words that occur more than 4 times"""
	for word in dictionary:
		if dictionary[word] > 4:
  			print word, dictionary[word]

getTopWords(oldwords_dict)
getTopWords(newwords_dict)

# Step 6. Print out important words
def readOut(filename, lst):
	"""Prints processed words out to new text files called oldwords_finished.txt and newwords_finished.txt"""
	fout = open(filename, 'w')
	for word in lst:
		fout.write(word +"\n")
	fout.close()

readOut("oldwords_finished.txt", oldwords)
readOut("newwords_finished.txt", newwords)

