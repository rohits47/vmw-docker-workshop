from collections import namedtuple
import sys
import getopt
import json
from pprint import pprint

error = ""

def parse_json(filename):
    with open(filename) as data_file:    
        return json.load(data_file)

def validate(paragraphs, sentences, words, tags):
       if (paragraphs > sentences):
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
    print "After validate", validation
    if (validation == False):
       return error
    print "Before parse"
    tweets = parse_json('tweets.json')
    output = []
    c = 0
    print "Tweet parse "
    for key in tweets:
        for data in tweets[key]:
            data["tweet_content"].replace("."," ")
            temp = data["tweet_content"].split(' ')
            output = output + temp 
            print output[c]
            c = c + 1
    print "Tweets string: \n" 
    sentencesPerPara = sentences/paragraphs
    wordsPerSentence = words/sentences
    print "per ", sentencesPerPara, " ", wordsPerSentence
    outLen = len(output)
    counter = 0
    final = ""
    print "printing final:"
    for i in range (0, paragraphs):
        for j in range (0, sentencesPerPara):
            for k in range (0, wordsPerSentence):
                final = final + output[counter % outLen] + " "
                counter = counter + 1
            final = final[:-1]
            final = final + ". "
            print final
        final = final + '\n\n'                                          
    print "final", final
    return final            
     
def main():
    data = parse_json('sample_input.json')
    pprint(data)
    paragraphs = data["paragraph"]
    words = data["word"]
    sentences = data["sentences"]
    tags = data["tags"]

    print("paragraphs: ", paragraphs, ", words: ", words, ", sentences: ", sentences, ", tags: ", tags, " test: ", )
    return text_generator(paragraphs, sentences, words, tags)

if __name__ == "__main__":
    main()

