import bottle
import pymongo
import sys


connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.test


def find():
    print "find one, reporting for duty"
    try:
        cursor = db.data.find()
    except:
        print "Unexpected error:", sys.exc_info()[0]

    all = []
    for doc in cursor:
        all.append(doc)
    return all

result = find()


@bottle.route('/')
def home_page():
    return bottle.template('html_template', username=result[0]["username"])

bottle.debug(True)
bottle.run(host='localhost', port=8080)