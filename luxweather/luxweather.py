#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy as tw
from lxml import etree
from config import keys
from config import settings

__title__ = 'luxweather'
__version__ = 'v.1.0.1'
__author__ = '@c0ding'
__repo__ = 'https://github.com/c0ding/luxweather'
__license__ = 'Apache v2.0 License'

forecast_location = settings['location']
temp_units = settings['units']

def get(data):
	""" Get the weather forecast from weather.yahoo.com. """
	forecast_url = "http://weather.yahooapis.com/forecastrss?u={0}&w={1}".format(temp_units, forecast_location)
	forecast_data = etree.parse(forecast_url)
	return forecast_data.xpath('string(/rss/channel/{})'.format(data), namespaces = {'yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0'})
(temp, condition) = (get('item/yweather:condition[1]/@temp'), get('item/yweather:condition[1]/@text'))
(day, low, high, text) = (get('item/yweather:forecast[1]/@day'), get('item/yweather:forecast[1]/@low'),get('item/yweather:forecast[1]/@high'), get('item/yweather:forecast[1]/@text'))

def post_tweet():
	""" Get everything on Twitter. """
	auth = tw.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
	auth.set_access_token(keys['access_token'], keys['access_secret'])
	api = tw.API(auth)
	try:
		tweet = "Today's weather conditions for #Luxembourg:\n\n" + "Current: " + "{0}°C and {1}".format(temp, condition) + "\n" + "Previsions: "+"low {0}°C, high {1}°C".format(low, high)
		api.update_status(tweet)
	except tw.TweepError as error:
		print "Error occured: %s" % error

if __name__ == '__main__':
	post_tweet()
