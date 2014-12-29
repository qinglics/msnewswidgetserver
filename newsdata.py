#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Data():

    def getData(self):
        ret = []
        ret.append(self.__wrapItem("http://www.cnn.com/2014/12/17/opinion/stanley-interview-threats/index.html?hpt=hp_t3", "Title", "Publisher", "Date", "http://img1.cache.netease.com/catchpic/4/4A/4AE0B96772F4EFDAF1CB6CB0BBEDEA9F.jpg"))
        ret.append(self.__wrapItem("http://www.cnn.com/2014/12/17/opinion/stanley-interview-threats/index.html?hpt=hp_t3", "As 'The Interview' is pulled, does this mean North Korea wins?", "CNN", "Dec. 17 2014", "http://img1.cache.netease.com/catchpic/4/4A/4AE0B96772F4EFDAF1CB6CB0BBEDEA9F.jpg"))
        ret.append(self.__wrapItem("http://www.insidercarnews.com/10-cars-that-are-being-discontinued-after-2015/?utm_source=yahoo&utm_medium=partner&utm_campaign=yahoo-all", "10 Cars That Are Being Discontinued After 2015", "CNN", "Oct. 31 2014", "http://img1.cache.netease.com/catchpic/4/4A/4AE0B96772F4EFDAF1CB6CB0BBEDEA9F.jpg"))
        ret.append(self.__wrapItem("http://money.cnn.com/2014/10/01/autos/ticket-magnets/?hpt=ob_articleallcontentsidebar&iid=obnetwork", "America's top 20 speeding ticket magnets", "CNN", "Oct. 1 2014", "http://img1.cache.netease.com/catchpic/4/4A/4AE0B96772F4EFDAF1CB6CB0BBEDEA9F.jpg"))
        ret.append(self.__wrapItem("http://news.qq.com/a/20141217/070665.htm?tu_biz=1.114.1.0", "调查称习近平认可度和本国人民信心度均排第一", "CNN", "Dec. 17 2014", "http://img1.cache.netease.com/catchpic/4/4A/4AE0B96772F4EFDAF1CB6CB0BBEDEA9F.jpg"))
        #ret.append(self.__wrapItem("url", "title", "CNN", "date", "http://img1.cache.netease.com/catchpic/4/4A/4AE0B96772F4EFDAF1CB6CB0BBEDEA9F.jpg"))
        
        
        return ret

    def __wrapItem(self, url, title, publisherName, date, newsImage):
        item = {}

        item['url'] = url
        item['title'] = title
        item['publisherName'] = publisherName
        item['date'] = date
        item['newsImage'] = newsImage
    
        return item

    
