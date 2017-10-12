'''import xml.dom.minidom as d

import copy
from collections import defaultdict

class Node(str):

    children = []
    def __index__(self, data):
        self.data = data
        self.children = []

    def addchildren(self, value):
        self.children.append(value)






sourceFileName = 'data.xml'
source = open(sourceFileName)
'''
import xml.dom.minidom

sourceFileName = 'data.xml'
source = open(sourceFileName)

dom = xml.dom.minidom.parse(source)

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handleSlideshow(slideshow):
    print ("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print ("</html>")

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print ("<title>%s</title>" % getText(title.childNodes))

def handleSlideTitle(title):
    print ("<h2>%s</h2>" % getText(title.childNodes))

def handlePoints(points):
    print ("<ul>")
    for point in points:
        handlePoint(point)
    print ("</ul>")

def handlePoint(point):
    print ("<li>%s</li>" % getText(point.childNodes))

def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print ("<p>%s</p>" % getText(title.childNodes))

handleSlideshow(dom)