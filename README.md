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
* Dean Dieker
* Miguael Bejar
* Davod OHayon 
* Eric Famiglietti
* Mike Laderman
* Evan Simpson 
* Alec Radford 
* Juliana Nazar&aecute;

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

Part 4. Short discussion of NLP
---

Lets take a look at these words together and decided which words we want to remove from our feed.
* Common words
* URLs
* Your name
* What else?
* Common Facebook acrynyms: kk, guys, hey

This is all part of the field of [Natural Language Processing (NLP)](http://en.wikipedia.org/wiki/Natural_language_processing), a field of computer science that deals with processing text and getting information out of it, as well as using information to make human-sounding text. For example, when you tweet at a bot on Twitter, it is often using NLP to process your tweet and respond to you in a human-sounding manner.

It's also very powerful becuase it allows you to get numerical statistics on text. For example:
* How many times did someone say my name?
* What is the word I use the most
* What words do people use the most (besides my name) when they talk to me?

You might find out that:
* Man, I only talk about sports
* I talk about homework a lot
* I use a ton of acrynyms (e.g. I found YOLO was a reoccuring word in my Facebook feed).
* I post a lot of URLs

Lets wait and see :)

Part 5. Lets start parsing your feed
---



