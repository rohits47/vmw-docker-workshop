from collections import namedtuple
import sys
import getopt
import json
from pprint import pprint
# from twitter_trends import generate_json_file

def str2bool(v):
  return v.lower() in ("true")

def parse_json(filename):
    with open(filename) as data_file:    
        return json.load(data_file)

def validate(paragraphs, sentences, words, tags):
    error = None
    if (paragraphs > sentences):
      error = "Error: Number of sentences is fewer than paragraphs"
    if (sentences > words):
      error = "Error: Number of sentences is fewer than paragraphs"
    if (words > 10000):
      error = "Error: Number of words is more than 10000"
    if (sentences > 1000):
      error = "Error: Number of sentences is greater than 1000"
    if (paragraphs > 100):
      error = "Error: Number of paragraphs is greater than 100"
    return error

def text_generator(paragraphs, sentences, words, htmltags):
    tags = str2bool(htmltags)
    validation = validate(paragraphs, sentences, words, tags)
    if validation:
      return validation
    # generate_json_file()
    tweets = parse_json('data.json')
    output = []
    for key in tweets:
        for data in tweets[key]:
            tmpStr = "".join(data["tweet_content"])
            tmpStr = tmpStr.replace("."," ")
            # print tmpStr
            temp = tmpStr.split(' ')
            output = output + temp 
    # if (__debug__):
        # print "Debug: Tweets string: \n"
    sentencesPerPara = sentences/paragraphs
    wordsPerSentence = words/sentences
    outLen = len(output)
    counter = 0
    final = ""
    excess = False
    for i in range (0, paragraphs):
        if (tags == True):
            final = final + "<p>"
        for j in range (0, sentencesPerPara):
            for k in range (0, wordsPerSentence):
                final = final + output[counter % outLen] + " "
                counter = counter + 1
                words = words - 1

            final = final[:-1]
            final = final + ". "
            sentences = sentences - 1
           # print final
        if (tags == True):
            final = final + "</p>"
        else:
           final = final + '\n\n'

    if (words != 0 or sentences != 0):
        excess = True
        if (tags == True):
            final = final[:-4]
        else:
            final = final[:-2]


    if (words != 0 and sentences != 0):
        while (sentences != 1):
            final = final + output[counter % outLen] + ". "
            counter = counter + 1
            sentences = sentences - 1
            words = words - 1
        while (words != 0):
            final = final + output[counter % outLen] + " "
            counter = counter + 1
            words = words - 1
        final = final +  "."
    elif (words!= 0):
        final = final[:-1]
        while (words != 0):
            final = final + output[counter % outLen] + " "
            counter = counter + 1
            words = words - 1
        final = final +  "."

    if (excess == True):
        if (tags == True):
            final = final + "</p>"
        else:
           final = final + '\n\n'
    # if (__debug__):
        # print "Debug: final\n", final
    return final            
     
# def main():
#     data = parse_json('input.json')
#     # pprint(data)
#     paragraphs = data["paragraph"]
#     words = data["word"]
#     sentences = data["sentences"]
#     tags = data["tags"]
#     if (__debug__):
#         # print("Debug: paragraphs: ", paragraphs, ", words: ", words, ", sentences: ", sentences, ", tags: ", tags, " test: ", )
#     return text_generator(int(paragraphs), int(sentences), int(words), bool(tags))

# if __name__ == "__main__":
#     main()

