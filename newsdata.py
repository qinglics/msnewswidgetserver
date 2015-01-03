#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import urllib2
from xml.dom import minidom
from time import strftime, strptime

class Data():

    def getData(self):
        rssContent = self.__getFileContent()
        return self.__getParsedData(rssContent)
		
    def __getParsedData(self, fileContent):
        xmldoc = minidom.parseString(fileContent)
        items = xmldoc.getElementsByTagName('item')
        tempImageUrl = "http://img1.cache.netease.com/catchpic/4/4A/4AE0B96772F4EFDAF1CB6CB0BBEDEA9F.jpg"

        ret = []
        for item in items:
            try:
                title = item.getElementsByTagName('title')[0].firstChild.nodeValue
                pubIndex = title.rfind('-')
                publisher = ""
                if pubIndex >= 0:
                    publisher = title[pubIndex+1:].strip()
                    title = title[0 : pubIndex].strip()
                    link = item.getElementsByTagName('link')[0].firstChild.nodeValue
                    dateStr = item.getElementsByTagName('pubDate')[0].firstChild.nodeValue
                    dateObj = strptime(dateStr, '%a, %d %b %Y %H:%M:%S %Z')
                    formatedDate = strftime('%b %d %Y', dateObj)

                    ret.append(self.__wrapItem(link, title, publisher, formatedDate, tempImageUrl))
            except Exception as e:
                print e

        return ret
		
    def __getFileContent(self):
        dfile = urllib2.urlopen(r'https://news.google.com/news?pz=1&cf=all&ned=cn&hl=zh-CN&output=rss')
        content = dfile.read()
        dfile.close()

        return content

    def __wrapItem(self, url, title, publisherName, date, newsImage):
        item = {}

        item['url'] = url
        item['title'] = title
        item['publisherName'] = publisherName
        item['date'] = date
        item['newsImage'] = newsImage
    
        return item
