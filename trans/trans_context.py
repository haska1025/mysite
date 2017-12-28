class Page(object):
  def __init__(self, t, u):
    self.title = t
    self.url = u 
 
class TransContext(object):
  def __init__(self, title):
    self.title = title 
    self.baseurl = '#'

  def setHeaderPages(self, pages):
    self.header_pages = pages;

