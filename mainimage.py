#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import urllib2

class MainImageOfUrl():

    def __init__(self, url):
        self.url = url

    def getImage(self):
        pageContent = self.__getUrlContent()

        return self.__getMainImage(pageContent)

    def __getMainImage(self, content):
        maxImgUrl = ""
        maxSize = 0
        if None == content:
            return maxImgUrl
        idx = content.find('<img ')
        while idx >= 0:
            try:
                wid = MainImageOfUrl.str2int(MainImageOfUrl.getValue(content, idx, 'width'))
                height = MainImageOfUrl.str2int(MainImageOfUrl.getValue(content, idx, 'height'))
                if height * 2 >= wid and wid * 2 >= height and wid * height > maxSize:
                    maxSize = wid * height
                    maxImgUrl = MainImageOfUrl.getValue(content, idx, 'src')
            except Exception as e:
                print e
            idx = content.find('<img ', idx + 1)

        return maxImgUrl
            
    @staticmethod
    def str2int(val):
        val = val.strip()
        idx = len(val)
        for i in range(0, len(val)):
            if False == val[i].isdigit():
                idx = i
                break
        return int(val[0:idx])
        
    @staticmethod
    def getValue(s, startIdx, attr):
        idx = s.find(attr+'=', startIdx)
        val = ''
        if idx >= startIdx:
            startIdx = idx + len(attr) + 2
            endIdx = s.find('"', startIdx)
            if endIdx > startIdx:
                val = s[startIdx : endIdx]
        return val

    def __getUrlContent(self):
        content = ""
        try:
            dfile = urllib2.urlopen(self.url)
            content = dfile.read()
            dfile.close()
        except Exception as e:
            print e

        return content


if '__main__' == __name__:
    
    def test(url, result):
        imgUrl = MainImageOfUrl(url).getImage()
        if imgUrl == result:
            print str(test.test_no) + ' pass'
        else:
            print str(test.test_no) + ' fail'
            print imgUrl

        test.test_no += 1
    test.test_no = 1
    print 'test'
    test('http://roll.sohu.com/20150104/n407502616.shtml', 'http://photocdn.sohu.com/20150104/Img407502619.jpg')
    test('http://www.jfdaily.com/guonei/new/201501/t20150104_1111896.html', 'http://images.jfdaily.com/jiefang/guonei/new/201501/W020150104423183200547.jpg')
    
