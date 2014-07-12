
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
scores = db.grades


def find():

    print "find, reporting for duty"

    query = {"type": 'homework'}

    try:

        cursor = scores.find(query)
        

        #cursor = cursor.sort('student_id', pymongo.ASCENDING)
        
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])



    except:
        print "Unexpected error:", sys.exc_info()[0]
    student_id = []
    for doc in cursor:
        if doc["student_id"] not in student_id:
            scores.remove(doc)
            student_id.append(doc["student_id"])

find()

