from bson import ObjectId
import pymongo
import os


class DbClient:
	def __init__(self, collection : str) :
		url = os.getenv('dbUrl')
		client = pymongo.MongoClient(url)
		database = client['project2']
		self.collection = database[collection]
  
	def getItems(self, id) : return self.collection.find({}) if id is None else self.collection.find( { '_id': ObjectId(id) } )

	def addNew(self, data) : self.collection.insert_one(data)
 
	def update(self, id, data) : self.collection.update_one( { '_id': ObjectId(id) }, data )
 
	def delete(self, id) : self.collection.delete_one( { '_id': ObjectId(id) } )