import azure.functions as func
import pymongo
from bson.objectid import ObjectId

from db_client import DbClient

client = DbClient('ads')

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            client.delete(id)

            return func.HttpResponse(id, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
