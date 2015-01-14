#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def getAbsoluteUrl(pageUrl, imgSrc):
    if None == imgSrc:
        return ""
    httpIdx = imgSrc.find('http')
    quoteIdx = imgSrc.find('://')
    if (httpIdx >= 0 and httpIdx <= 10) or (quoteIdx >= 0 and quoteIdx <= 10):
        return imgSrc
    
    parts = []
    level = 0
    splits = imgSrc.split('/')
    for s in splits:
        ss = s.strip()
        if len(ss) == 0:
            continue
        
        if '.' == ss:
            pass
        elif '..' == ss:
            if len(parts) > 0:
                parts.pop()
            else:
                level += 1
        else:
            parts.append(ss)
    
    while level >= 0:
        idx = pageUrl.rfind('/')
        if idx >= 0:
            pageUrl = pageUrl[0:idx]
            level -= 1
        else:
            break
        
    return pageUrl + '/' + '/'.join(parts)


if '__main__' == __name__:
    def test(pageUrl, imgSrc, expected):
        result = getAbsoluteUrl(pageUrl, imgSrc)
        if result == expected:
            print 'pass'
        else:
            print 'fail'
            print result
            
    test('http://www.baidu.com/1/2/3/test.html', 'abc.image', 'http://www.baidu.com/1/2/3/abc.image')
    test('http://www.baidu.com/1/2/3/test.html', '../../image.jpg', 'http://www.baidu.com/1/image.jpg')
    test('http://www.baidu.com/1/2/3/test.html', '../test/../image.jpg', 'http://www.baidu.com/1/2/image.jpg')
    test('http://www.baidu.com/1/2/3/test.html', '../test/../../image.jpg', 'http://www.baidu.com/1/image.jpg')
    test('http://www.baidu.com/1/2/3/test.html', 'http://www.baidu.com/test/ab.jpg', 'http://www.baidu.com/test/ab.jpg')
    