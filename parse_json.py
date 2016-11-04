from collections import namedtuple
import sys
import getopt
import json
from pprint import pprint

final = ""
error = ""

def parse_json(filename):
    with open(filename) as data_file:    
        return json.load(data_file)

def validate(paragraphs, sentences, words, tags):
       if (paragraphs < sentences):
               error = "Number of sentences is fewer than paragraphs"
               return False
       if (words > 10000):
               error = "Number of words is more than 10000"
               return False
       if (sentences > 1000):
               error = "Number of sentences is greater than 1000"
               return False
       if (paragraphs > 100):
               error = "Number of paragraphs is greater than 100"
               return False
       return True

def text_generator(paragraphs, sentences, words, tags):
    print("Validates input and generates text from tweets.json")
    validation = validate(paragraphs, sentences, words, tags)
    if (validation == False):
       return error
    tweets = parse_json('tweets.json')
    output = [] 
    for key in tweets:
        for data in tweets[key]:
            data["tweet_content"].replace("."," ")
            temp = data["tweet_content"].split(' ')
            output = output + temp 
    print "Tweets string: \n" 
    print output        
    
    sentencePerPara = sentences/paragraphs
    wordsPerSentence = words/sentence
    outLen = len(output)
    counter = 0
    for i in range (0, paragraphs):
        for j in range (0, sentences):
            for k in range (0, words):
                
                

def main():
    data = parse_json('input.json')
    pprint(data)
    paragraphs = data["paragraph"]
    words = data["word"]
    sentences = data["sentences"]
    tags = data["tags"]

    #print("paragraphs: ", paragraphs, ", words: ", words, ", sentences: ", sentences, ", tags: ", tags, " test: ", )
    return text_generator(paragraphs, sentences, words, tags)

if __name__ == "__main__":
    main()

