High School RampUp: The Docs
=========

Intro
---
Hey guys, welcome to High School RampUp! Get excited, we are going to teach you how to use code to analyze your Facebook news feed.

A few questions we are going to help you answer through code:
1. What did I say on Facebook two years ago?
2. What do I say on Facebook today?
3. How'd my language on Facebook change over time?

Meet the Mentors
---
Before we get started, I want to introduce you to the people who are here to help teach.
* David Ohayon 
* Eric Famiglietti
* Evan Simpson 
* Alec Radford 
* Juliana Nazar&eacute;

Please raise your hand as soon as you have any questions and we will come help.

Part 0. Grab your Facebook feed
---
Awesome, lets start. Please go to [My Feed Scraper](http://myfeedscraper.herokuapp.com) and log in using your Facebook. Please give it all the permissions it requests for. It will take a minute or so to load all your Facebook data.
* If you did not have a Facebook two years ago, raise your hand.
* If you do not have a Facebook or want to log into your Facebook, raise your hand.

Part 1. Download the materials
---
Please go to the [High School RampUp Github Page](https://github.com/rampup/hs-rampup) and click the __ZIP___ button. This will download the all the files you need to get started as a zip file. Double click on the download to unzip it and move it to your Desktop (or another location on your computer that you prefer).

Part 2. Make your text files
---
Open up your text editor (Sublime or another editor). Go to File --> Open and navigate to the HS-RampUp folder (the one you just downloaded). 

Open up __oldwords.txt__ and __newwords.txt__

Copy/paste your text from My Feed Scraper into the two text files. Paste your Facebook feed text from 2 years ago into __oldwords.txt__ and your present Facebook feed text into __newwords.txt__ and delete the text in ALL CAPS at the top of both text files.

Part 3. Let's talk about language processing
---

Take a minute to look through your Facebook feed text files. What words jump out to you as commonplace? What words do you think will occur most often?

Go up to the board and write down 5 words that you think will come up most often. If someone has already written down your word, write down a different one.

Part 4. Short discussion of Natural Langauge Processing
---

Lets take a look at these words together and decide which words we want to remove from our feed.
* Common words
* URLs
* Your name
* What else?
* Common Facebook acrynyms: kk, brb, "hey guys", ya'll

This is all part of the field of [Natural Language Processing (NLP)](http://en.wikipedia.org/wiki/Natural_language_processing), a field of computer science that deals with processing text and getting information out of it, as well as using information to make human-sounding text. For example, when you tweet at a bot on Twitter, it is often using NLP to process your tweet and respond to you in a human-sounding manner.

It's also very powerful becuase it allows you to get numerical statistics on text. For example:
* How many times did someone say my name?
* What is the word I use the most
* What words do people use the most (besides my name) when they talk to me?

You might find out that:
* Man, I only talk about sports
* I talk about homework a lot
* I use a ton of acrynyms (e.g. I found SI (the acronym for Startup Institute) was a reoccuring word in my Facebook feed).
* I post a lot of URLs

Lets wait and see :)

Part 5. Lets start parsing your feed
---
Everyone is going to choose to parse their word feed differently. To start off, we will walk through an example of how to loop through and have your computer "read" your Facebook feed's text. 

```
for word in newwords:
	print word
```

This is an example of a basic for loop that iterates through each word seen and prints out each word individually. You can think about for loops like Easter Eggs. You can dye all your Easter Eggs at once, but for maximum effect, you want to pick up each one indivdually, "process it", and put it back to dry. In Computer Science, this would be called iterating through the Easter Eggs.

Now, we can put that inside of a __function__ so that we only have to type it one and can resuse it. You can think about a function as a tube that you cannot see inside. You put an __arguement__, (in the case below called "lst") into the box on one side and out drops a returned object, which is different than the argument. For example, in the code below, I put a list of words into the tube and the tube "operated on them" and returned "done!" when it finished running.

```
def printWords(lst):
	for word in lst:
		print word
	return "done!"

printWords(oldwords)
printWords(newwords)
```

Now we are going to talk to you about how to remove a word from your list of words.

```
def removeWords(lst):
	for word in lst:
		if word == "startup":
			lst.remove(word)
```


-- define a variable
-- define a function
-- define a for and if loop
-- define a list
-- define removing items from a list
-- * define a dictionary

-- Takeaway: programming is very powerful. You can process a lot of data quickly and visualize it in a way to get information out. Imagine all the math problems you do. They can all be done programatically You don't have to go through 10 steps of alegebra if you can solve it with a computer. 

-- The stuff you did today -- its the start of how all your favorite web apps (Facebook, Twitter, Google) take user data and process it to understand what the general population is thinking. For example, think about how you get "promoted posts" on Facebook -- those are specifically targeted to you. Facebook does this by analyzing who you are programatically and then trying to match your interests to one in a promotion.





