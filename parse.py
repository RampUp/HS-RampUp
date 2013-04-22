# Step 0. Load both text files
# Testing. Print out all the text
def readIn(filename):
	"""Takes in filename. Returns array of words in file"""
	with open(filename, 'r') as myfile:
		words = myfile.read().replace('\n', ' ')
	return words.split()

oldwords = readIn("oldwords.txt")
newwords = readIn("newwords.txt")

# Step 1. Iterate through the text files
# Testing. Print out all the text

# Step 2. Remove your name
# Testing. Print out "Removed! + word removed"

# Step 3. Remove common words
# Testing. Print out "Removed! + word removed"

# Step 4. Count how often each word appears
# Testing. Print out "Count + word"

# Step 5. Organize words so that the most common is first
# Testin. Print out "Count + word"

# Step 6. Print out important words
def readOut(filename, lst):
	"""Prints processed words out to new text files called oldwords_finished.txt and newwords_finished.txt"""
	fout = open(filename, 'w')
	for word in lst:
		fout.write(word +"\n")
	fout.close()

readOut("oldwords_finished.txt", oldwords)
readOut("newwords_finished.txt", newwords)
