import urllib
import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup


if __name__ == "__main__":
    cj = http.cookiejar.CookieJar()
    c1 = http.cookiejar.Cookie(version=0, name='uid',
        value='7530',
        port=None, port_specified=False,
        domain='tracker.maxnet.ua',
        domain_specified=True,
        domain_initial_dot=True, path='/',
        path_specified=True, secure=False,
        expires=None, discard=True, comment=None,
        comment_url=None, rest={'HttpOnly': None})
    c2 = http.cookiejar.Cookie(version=0, name='pass',
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
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    headers =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib.request.Request('http://tracker.maxnet.ua/details.php?id=76590', None, headers)
    res = opener.open(request)
    soup = BeautifulSoup(res.read().decode('cp1251'))

    for link in soup.find_all('strong'):
        print(link)