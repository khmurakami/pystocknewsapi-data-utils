#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from pystocknewsapi import NewsStreamer

# Insert your own key as a string here
API_KEY = os.environ['STOCK_NEWS_API_KEY']

class PyStockNewsAPIData():

    def __init__(self, API_KEY):

        self.streamer = NewsStreamer(API_KEY)


    # https://www.mapillary.com/developer/api-documentation/#pagination
    def get_recent_general_news_article(self, source):

        """Get the most recent general news article based on source

        Args:
            source

        Return:
            recent_news (json dict): The most recent news as a dict

        """

        raw_json = self.streamer.get_general_market_news()
        recent_news = raw_json["data"][0]

        return recent_news

    def stocknewsapi_csv_list_create(self, csv_name, ):

        """Create a CSV dataset based on the source

        Args:
            csv_name (string): Name of the csv you want to create


        Return:
            None

        """

        pass
