# DONT TOUCH -- Step 0. Read in files
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




# Step 1. Iterate through the text files and print out the text
def printlist(lst):
	"""Neatly print out a list"""
	pass

# TESTCASE: printlist(oldwords + newwords)



# Step 2. Remove your name
def removeName(lst, name):
	"""Remove name from list and return processed list"""
	name = "" # Put your name here
	pass

# Testing. Print out "Removed! + word removed"
# TESTCASE: oldwords = removeName(oldwords, "Juliana")
# TESTCASE: newwords = removeName(newwords, "Juliana")



# Step 3. Remove punctuation
def removePunctuation(lst):
	"""Removes all punctiation and returns processed list"""
	punctuation = ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', ':', ';']
	pass

# Testing. Print our "Removed! + word removed"
# TESTCASE: oldwords = removePunctuation(oldwords)
# TESTCASE: newwords = removePunctuation(newwords)



# Step 4. Remove common words
def removeCommonWords(lst):
	"""Removes all words in commons.txt from list and returns processed list"""
	commons = getCommonWords()
	pass

# Testing. Print out "Removed! + word removed"
# TESTCASE: oldwords = removeCommonWords(oldwords)
# TESTCASE: newwords = removeCommonWords(newwords)



# Step 5. Remove URLs
def removeURLs(lst):
	"""Removes all urls and returns processed list"""
	pass

# Testing. Print out "Removed + url removed"
# TESTCASE: oldwords = removeURLs(oldwords)
# TESTCASE: newwords = removeURLs(newwords)



# Step 6. Count how often each word appears
def countUpWords(lst):
	"""Creates a freqency table for the number of times that a word appears"""
	pass

# Testing. Print out "Count + word"
# TESTCASE: oldwords_dict = countUpWords(oldwords)
# TESTCASE: newwords_dict = countUpWords(newwords)



# Step 7. Get top words
def getTopWords(dictionary):
	"""Prints out words that occur more than 4 times"""
	pass

# Testing. Print out "Count + word"
# TESTCASE: getTopWords(oldwords_dict)
# TESTCASE: getTopWords(newwords_dict)


# DONT TOUCH -- Step 8. Print out important words
def readOut(filename, lst):
	"""Prints processed words out to new text files called oldwords_finished.txt and newwords_finished.txt"""
	fout = open(filename, 'w')
	for word in lst:
		fout.write(word +"\n")
	fout.close()

readOut("oldwords_finished.txt", oldwords)
readOut("newwords_finished.txt", newwords)

