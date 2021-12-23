import requests, random

def getWordList():
	word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
	response = requests.get(word_site)
	return response.content.splitlines()

def pickRandomWord(wordlist):
	return wordlist[random.randint(0,len(wordlist))]

WORDS = getWordList()
print(pickRandomWord(WORDS))