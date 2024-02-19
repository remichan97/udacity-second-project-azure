import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from db_client import DbClient

client = DbClient('post')

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        data = client.getItems()
        result = dumps(data)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)