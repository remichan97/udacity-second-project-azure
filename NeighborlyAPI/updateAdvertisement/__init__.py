import azure.functions as func
import pymongo
from bson.objectid import ObjectId

from db_client import DbClient

client = DbClient('advertisements')

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            update_query = {"$set": eval(request)}
            client.update(id, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

