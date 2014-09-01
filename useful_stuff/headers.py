#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
manual: http://www.tutorialspoint.com/python/python_cgi_programming.htm
"""
# Content-Type & Cache
# import datetime
# expires = datetime.datetime.utcnow() + datetime.timedelta(days=1)
# expires = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
# print('Last-Modified: Mon, 01 Sep 2014 10:33:10 GMT')
# print('Expires: ' + expires)

# Cookie
print('Set-Cookie: user=Vitaliy;')

# text/html
print('Content-Type: text/plain;charset=utf-8\r\n\r\n')

# CGI Environment Variables
import os
for param in os.environ.keys():
    print('%20s: %s' % (param, os.environ[param]))

# Forms/get/post data
import cgi
form = cgi.FieldStorage()
print(form)