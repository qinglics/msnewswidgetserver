#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

encodings = ['utf-8', 'gb2313', 'ascii', 'gbk', 'iso-8859-1']

def detectCoding(webPageContent):
    if None == webPageContent or len(webPageContent) == 0:
        return ""
    webPageContent = webPageContent.lower()
    code = getValue(webPageContent, 'charset=')
    if len(code) > 0:
        return code
    code = getValue(webPageContent, 'encoding=')
    if len(code) > 0:
        return code
    for i in range(0, len(encodings)):
        try:
            webPageContent.decode(encodings[i])
            return encodings[i]
        except Exception as e:
            pass

    return ""

def getValue(content, attr):
    idx = content.find(attr)
    if idx >= 0:
        idx += len(attr)
        if content[idx] == '"' or content[idx] == '\'':
            idx += 1
        endIdx = idx
        for i in range(idx, len(content)):
            if not content[i].isalnum() and not '-' == content[i]:
                endIdx = i
                break
        if endIdx == idx:
            endIdx = len(content)
        return content[idx : endIdx]
    return ""

if '__main__' == __name__:
    def test(content, result):
        if detectCoding(content) == result:
            print 'pass'
        else:
            print 'fail'
            print detectCoding(content)


    test("Content-Type: text/html; charset=ISO-8859-4", "iso-8859-4")
    test('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">', 'utf-8')
    test('html; charset="utf-8">', 'utf-8')
    test('html; charset="utf-8>', 'utf-8')
    test('html; charset="utf-8 >', 'utf-8')
    test('html; encoding="utf-8">', 'utf-8')
    test('html; encoding="utf-8>', 'utf-8')
    test('html; encoding="utf-8 >', 'utf-8')
