#!/usr/bin/python
"""
Copyright 2016 VMware, Inc. All rights reserved. -- VMware Confidential
twitter-trends -- lists the current global trending topics
This module will get the top 10 trending topics for the specific [WODID], if trending information is available for it.

The response is an array of "trend" objects that encode the name of the trending topic, the query parameter that can be
used to search for the topic on Twitter Search (https://dev.twitter.com/apps/13054031/oauth), and the Twitter Search URL.

This information is cached for 5 minutes, Requesting more frequently than that will not return any more data, and will
count against your rate limit usage.
"""

from twitter import *
import json
import logging
from LoggerManager import LoggerManager
import constans
import urllib2

log = LoggerManager().getLogger("__twitter_trends_log__")
log.setLevel(level=logging.INFO)
log.info("*******************************")
log.info("*                             *")
log.info("* ExtractTwitterTrends module* ")
log.info("*                             *")
log.info("*******************************")


def load_twitter_api_credentials():
    """
    get all the api credentials from the config file
    :return: all the tokens for twitter api
    """
    # load our API credentials
    config = {}
    try:
        execfile("config.py", config)
    except Exception as e:
        msg = "Exception occurred when read the twitter api credentials config file!"
        log.info(msg + str(e))
        raise
    return config


def retrieve_catagory_twitter_trends():
    """
    This function will retrieve all the categories base on the WODID
    :return: the dictionary which contain all the top 10 tweets in specific category
    """
    config = load_twitter_api_credentials()
    # create twitter API object
    twitter = Twitter(
        auth=OAuth(config[constans.TwitterOAuth.ACCESS_KEY], config[constans.TwitterOAuth.ACCESS_SECRET],
                   config[constans.TwitterOAuth.CONSUMER_KEY], config[constans.TwitterOAuth.CONSUMER_SECRET]))
    # -----------------------------------------------------------------------
    # retrieve global trends.
    # other localised trends can be specified by looking up WOE IDs:
    # http://developer.yahoo.com/geo/geoplanet/
    # twitter API docs: https://dev.twitter.com/docs/api/1/get/trends/%3Awoeid
    # -----------------------------------------------------------------------
    results = twitter.trends.place(_id=constans.WODID)
    # TODO: for the basic version, only provide one catagory twitter
    all_tweet_dict = {}
    for location in results:
        top_3_trends = 1
        log.info("Tweet trends in %s !" % location)
        for trend in location[constans.TRENDS]:
            top_3_trends += 1
            log.info("The name of current tweet trend is %s" % trend[constans.NAME])
            # parse the top 3 tweets base on the category and the url
            all_tweet_dict[trend[constans.NAME]] = retrieve_top5_tweet_from_catagory(category=trend[constans.NAME],
                                                                                     category_url=trend[constans.URL],
                                                                                     twitter=twitter)
            if top_3_trends > 3:
                break
    return all_tweet_dict

def retrieve_top5_tweet_from_catagory(category=None, category_url=None, twitter=None):
    """
    Parse the top 5 tweets for specific category
    :param category: tweet-category
    :param category_url: url for the current category
    :return: top 10 tweets in current category
    """
    # check the validation of the parameters
    num_tweet = 1
    results = []
    if category is None or category_url is None or twitter is None:
        log.info("Please check the twitter category and the url!")
        return results
    response = urllib2.urlopen(category_url)
    data = response.readlines()
    for line in data:
        tweet_dict = {}
        if constans.DATA_TWEET_ID in line:
            tweet_id = line.split("\"")[1]
            try:
                current_tweet = twitter.statuses.show(id=tweet_id)
                log.info("--The current tweet id is %s" % current_tweet[constans.TWEET_ID_STR])
                log.info("-- The current tweet contect is %s" % current_tweet[constans.TWEET_TEXT])
                tweet_dict[constans.TWEET_NAME] = current_tweet[constans.TWEET_ID_STR]
                tweet_dict[constans.TWEET_CONTENT] = current_tweet[constans.TWEET_TEXT]
                results.append(tweet_dict)
                num_tweet += 1
                if num_tweet > 5:
                    break
            except Exception as e:
                msg = str(e)
                log.info(msg)
    return results


def generate_json_file():
    """
    This function will generate json file
    :return: output is the content of tweets in json format
    """
    data = retrieve_catagory_twitter_trends()
    with open(constans.DATA_OUTPUT, 'w') as outfile:
        json.dump(data, outfile)

generate_json_file()
