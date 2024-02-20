from bson import ObjectId
import pymongo
import os


class DbClient:
	def __init__(self, collection : str) :
		# url = os.getenv('dbUrl')
		url = 'mongodb+srv://mirai:Remichan%40admin@udacity-cosmos.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000'
		client = pymongo.MongoClient(url)
		database = client['project2']
		self.collection = database[collection]
  
	def getItems(self, id = None) : return self.collection.find({}) if id is None else self.collection.find( { '_id': ObjectId(id) } )

	def addNew(self, data) : self.collection.insert_one(data)
 
	def update(self, id, data) : self.collection.update_one( { '_id': ObjectId(id) }, data )
 
	def delete(self, id) : self.collection.delete_one( { '_id': ObjectId(id) } )