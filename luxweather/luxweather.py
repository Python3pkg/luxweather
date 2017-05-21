#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib.request, urllib.error, urllib.parse
import tweepy as tw
from config import settings

__title__ = 'luxweather'
__version__ = 'v.1.1'
__author__ = 'Martin Simon <me@martinsimon.me>'
__repo__ = 'https://github.com/mrsmn/luxweather'
__license__ = 'Apache v2.0 License'

BASE_URL = "https://api.darksky.net/forecast/{0}/{1},{2}?units=si&exclude=minutely,hourly,alerts,flags".format(settings['darksky_api_key'], settings['latitude'], settings['longitude'])

def _http_get():
    opener = urllib.request.build_opener()
    opener.addheaders.append(('Content-Type', 'application/json'))
    opener.addheaders.append(('User-agent', 'luxweather - Twitter weather bot written in Python. (https://github.com/mrsmn/luxweather)'))
    response = opener.open(BASE_URL).read()
    return response

def post():
    data = json.loads(_http_get())
    low = int(data["currently"]["temperature"])
    condition = data["currently"]["summary"]
    daily_min = int(data["daily"]["data"][0]["temperatureMin"])
    daily_max = int(data["daily"]["data"][0]["temperatureMax"])
    auth = tw.OAuthHandler(settings['twitter_consumer_key'], settings['twitter_consumer_secret'])
    auth.set_access_token(settings['twitter_access_token'], settings['twitter_access_secret'])
    api = tw.API(auth)
    try:
        tweet = "Today's weather conditions for #Luxembourg:\n\n" + "Current: " + "{0}°C, {1}".format(low, condition) + "\n" + "Previsions: "+"low {0}°C, high {1}°C".format(daily_min, daily_max)
        api.update_status(tweet)
    except tw.TweepError as error:
        print("Error occured: {0}".format(error))

if __name__ == '__main__':
    post()
