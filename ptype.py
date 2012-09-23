import urllib2
import re

def html_from_url(url):
    #url = 'http://en.wikipedia.org/wiki/Memcached'
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')
    response = urllib2.urlopen(request)
    doc = response.read()
    #doc = unicode(doc,'utf-8')#alex martelli said this
    return doc


html = html_from_url('http://google.com/search?q=google')
regex = re.compile(r'<li class="g">.*?</li>')
match = re.findall(regex,html)
each =  match[0]

f1 = open('test.html','w')
#for each in match:
f1.write(each)
f1.close()

