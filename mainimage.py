#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import urllib2
import imageurls
from encoding import detectCoding
import threading
from getimagesize import ImageSize

def getSizeOfImage(url):
    try:
        return ImageSize(url).getXYOfImage()
    except Exception as e:
        print e
    return (0, 0)

def getImageSizeThread(url, imgsWithSize):
    try:
        imgsWithSize[url] = getSizeOfImage(url)
    except Exception as e:
        print e

class MainImageOfUrl():

    def __init__(self, url):
        self.url = url

    def getImage(self):
        pageContent = self.__getUrlContent()
        return self.__getMainImage(pageContent)

    def __getMainImage(self, content):
        (imgsWithSize, orderedUrl) = self.__getImgWithSize(content)
        print imgsWithSize
        threads = []
        for url in imgsWithSize.keys():
            t = None
            if None == imgsWithSize[url]:
                t = threading.Thread(target=getImageSizeThread, args=(url, imgsWithSize))
            elif 2 != len(imgsWithSize[url]):
                t = threading.Thread(target=getImageSizeThread, args=(url, imgsWithSize))
            elif 0 == imgsWithSize[url][0] or 0 == imgsWithSize[url][1]:
                t = threading.Thread(target=getImageSizeThread, args=(url, imgsWithSize))
            if None != t:    
                threads.append(t)
        
        for t in threads:
            try:
                t.start()
            except Exception as e:
                pass
        for t in threads:
            try:
                t.join(10)
            except Exception as e:
                print e
        
        
        if len(imgsWithSize) == 0:
            return ""
        biggestUrl = ""
        biggestSize = 0
        for url in orderedUrl:
            width = imgsWithSize[url][0]
            height = imgsWithSize[url][1]
            if min(width, height) * 2 >= max(width, height):
                if width * height > biggestSize:
                    biggestSize = width * height
                    biggestUrl = url
        return biggestUrl

    def __getImgWithSize(self, content):
        ret = {}
        maxSize = 0
        if None == content:
            return (ret, [])
        idx = content.find('<img ')
        orderedUrl = []
        while idx >= 0:
            try:
                wid = MainImageOfUrl.str2int(MainImageOfUrl.getValue(content, idx, 'width'))
                height = MainImageOfUrl.str2int(MainImageOfUrl.getValue(content, idx, 'height'))
                if min(height, wid) * 2 >= max(height, wid) and wid * height > maxSize:
                    imgUrl = imageurls.getAbsoluteUrl(self.url, MainImageOfUrl.getValue(content, idx, 'src'))
                    ret[imgUrl] = (height, wid)
                    orderedUrl.append(imgUrl)
                elif 0 == min(wid, height):
                    imgUrl = imageurls.getAbsoluteUrl(self.url, MainImageOfUrl.getValue(content, idx, 'src'))
                    ret[imgUrl] = (height, wid)
                    orderedUrl.append(imgUrl)
            except Exception as e:
                print e
            idx = content.find('<img ', idx + 1)

        return (ret, orderedUrl)
            
    @staticmethod
    def str2int(val):
        val = val.strip()
        if val.find('%') >= 0:
            return 0
        idx = len(val)
        for i in range(0, len(val)):
            if False == val[i].isdigit():
                idx = i
                break
        if idx > 0:
            return int(val[0:idx])
        return 0
        
    @staticmethod
    def getValue(s, startIdx, attr):
        idx = s.find(attr+'=', startIdx)
        val = ''
        if idx >= startIdx:
            startIdx = idx + len(attr) + 2
            endIdx1 = s.find('"', startIdx)
            endIdx2 = s.find('\'', startIdx)
            endIdx = max(endIdx1, endIdx2)
            if endIdx1 >= 0 and endIdx2 >= 0:
                endIdx = min(endIdx1, endIdx2)
            if endIdx > startIdx:
                val = s[startIdx : endIdx]
        return val

    def __getUrlContent(self):
        content = ""
        try:
            dfile = urllib2.urlopen(self.url)
            content = dfile.read()
            dfile.close()
            try:
                coding = detectCoding(content)
                if len(coding) >= 0: # default is utf-8
                    content = content.decode(coding).encode('UTF-8')
            except Exception as e:
                print e
        except Exception as e:
            print e

        return content


if '__main__' == __name__:
    
    def test(url, result):
        imgUrl = MainImageOfUrl(url).getImage()
        if imgUrl == result:
            test.result.append(' pass')
        else:
            test.result.append(' fail')
            print imgUrl

    test.result = []
    print 'test'
    test('http://roll.sohu.com/20150104/n407502616.shtml', 'http://photocdn.sohu.com/20150104/Img407502619.jpg')
    test('http://www.jfdaily.com/guonei/new/201501/t20150104_1111896.html', 'http://images.jfdaily.com/jiefang/guonei/new/201501/W020150104423183200547.jpg')
    test('http://money.cnn.com/2015/01/13/technology/security/cameron-messaging-data/index.html', 'http://i2.cdn.turner.com/money/dam/assets/150113091043-cameron-messaging-data-620xa.jpg')
    #test('', '')
    test('http://mobile.163.com/15/0112/07/AFOAH0670011179O.html#index_digi_1', 'http://img1.cache.netease.com/catchpic/9/98/98A017FB7CC3EC9ABA73073E84A10657.jpg')
    test('http://www.cnn.com/2015/01/13/asia/airasia-disaster/index.html', 'http://i2.cdn.turner.com/cnnnext/dam/assets/150114091745-01-airasia-0114-super-169.jpg')
    
    for i in range(0, len(test.result)):
        print "test " + str(i+1) + test.result[i]
