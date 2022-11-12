from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://tmdgy9272:dltmdgy1@cluster0.ey8kvzl.mongodb.net/?retryWrites=true&w=majority')
db = client.tmdgy9272

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})
