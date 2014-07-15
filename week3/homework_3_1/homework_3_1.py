
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students


def find():

    print "find, reporting for duty"

    query = {"type": 'homework'}

    cursor = students.find()
    for doc in cursor:
        homework = filter(lambda x: x["type"] == "homework", doc["scores"])
        score_to_remove = min(homework, key=lambda x: x["score"])
        doc["scores"].remove(score_to_remove)
        students.save(doc)
find()

