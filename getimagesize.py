'''
@author: qlyp
'''

import urllib2
from PIL import Image
from StringIO import StringIO

class ImageSize(object):
    '''
    input: url of an image
    output: height and width of the image
    '''


    def __init__(self, imageUrl):
        '''
        Constructor
        '''
        self.imageUrl = imageUrl
        
        
    def __getContent(self):
        dfile = urllib2.urlopen(self.imageUrl)
        content = dfile.read()
        dfile.close()

        return content
    
    def getXYOfImage(self):
        imgContent = self.__getContent()
        im = Image.open(StringIO(imgContent))
        return im.size
        
        
if '__main__' == __name__:
    def test(imgUrl, x, y):
        result = ImageSize(imgUrl).getXYOfImage()
        if result[0] == x and result[1] == y:
            print 'pass'
        else:
            print 'fail'
    
    test('http://img1.cache.netease.com/cnews/2015/1/12/20150112074929bf70f.jpg', 310, 220)
    test('http://img3.cache.netease.com/photo/0001/2015-01-13/AFREP30I3R710001.jpg', 1440, 960)
    test('http://img5.cache.netease.com/cnews/2015/1/13/201501130910196404b.jpg', 550, 413)
            
