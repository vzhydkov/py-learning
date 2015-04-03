#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
import csv
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class LibraryChild(Base):
    __tablename__ = 'LIBRARY_CHILD'

    ID = Column(Integer, primary_key=True)
    LIBRARY_ID = Column(Integer)
    OFFICIAL_NAME = Column(String)

    def __init__(self, LIBRARY_ID, OFFICIAL_NAME):
        self.LIBRARY_ID = LIBRARY_ID
        self.OFFICIAL_NAME = OFFICIAL_NAME

    def __repr__(self):
        return "<User('%s')>" % (self.OFFICIAL_NAME)

DEBUG = True
errors = ''
message = ''
form = cgi.FieldStorage()
if 'file_name' in form:
    fileitem = form['file_name']
    if fileitem.filename:
        if form.getvalue('library_id'):
            library_id = form.getvalue('library_id')
            if DEBUG:
                result = []
                for rows in csv.reader(fileitem.file):
                    for child_name in rows:
                        result.append('(NULL , '+library_id+', "'+child_name.strip()+'")')
                if result:
                    message = 'INSERT INTO LIBRARY_CHILD (ID, LIBRARY_ID, OFFICIAL_NAME) VALUES ' + ', '.join(result) + ';'
                else:
                    message = 'File empty or wrong format'
            else:
                engine = create_engine("mysql+mysqldb://root:zxcv2783@/RBDG")
                Session = sessionmaker(bind=engine)
                session = Session()
                for rows in csv.reader(fileitem.file):
                    for child_name in rows:
                        child = LibraryChild(library_id, child_name.strip())
                        session.add(child)
                session.commit()
                fn = os.path.basename(fileitem.filename)
                message += 'The file "' + fn + '" was uploaded successfully<br />'
        else:
            errors += 'No library id<br />'
    else:
       errors += 'No file was uploaded<br />'

if not message:
    message = '<form action="child_lib.py" method="post" enctype="multipart/form-data">' \
              'Library id: <input type="text" name="library_id" /><br />' \
              'Scv file: <input type="file" name="file_name" /><br />' \
              '<input type="submit" value="Upload" /><br />' \
              '</form>'

html = '<html>' \
       '<head>' \
       '<title>Import child page</title>' \
       '</head>' \
       '<body>' \
       '<h2>Child libraries import</h2>' \
       + errors + message + \
       '</body>' \
       '</html>'

print('Content-type:text/html\r\n\r\n')
print(html)