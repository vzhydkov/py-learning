from bs4 import BeautifulSoup
try:
    import urllib2 as urllib
except ImportError:
    import urllib
try:
    import http.cookiejar as cookielib
except ImportError:
    import cookielib

cj = cookielib.CookieJar()
c1 = cookielib.Cookie(version=0, name='uid',
                      value='7530',
                      port=None, port_specified=False,
                      domain='tracker.maxnet.ua',
                      domain_specified=True,
                      domain_initial_dot=True, path='/',
                      path_specified=True, secure=False,
                      expires=None, discard=True, comment=None,
                      comment_url=None, rest={'HttpOnly': None})
c2 = cookielib.Cookie(version=0, name='pass',
                      value='bfd543fc40cd9e953845fd4239086255',
                      port=None, port_specified=False,
                      domain='tracker.maxnet.ua',
                      domain_specified=True,
                      domain_initial_dot=True, path='/',
                      path_specified=True, secure=False,
                      expires=None, discard=True, comment=None,
                      comment_url=None, rest={'HttpOnly': None})
cj.set_cookie(c1)
cj.set_cookie(c2)
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]

# for py2 need import urllib
# values = {'name': 'Michael Ford',
#           'location': 'Northampton',
#           'language': 'Python'}
# data = urllib.urlencode(values)

response = opener.open('http://tracker.maxnet.ua/details.php?id=76590')
soup = BeautifulSoup(response.read().decode('cp1251'))

for link in soup.find_all('strong'):
    print(link)
