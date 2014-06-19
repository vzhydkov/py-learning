#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgitb
cgitb.enable()
print('Content-Type: text/plain;charset=utf-8')

"""
apache + python: https://docs.python.org/2/howto/webservers.html
<Directory "path">
     Options +ExecCGI
     AddHandler cgi-script .cgi .py
     Order allow,deny
     Allow from all
</Directory>
"""