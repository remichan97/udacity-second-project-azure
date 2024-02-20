from unittest import result
import azure.functions as func
from bson.json_util import dumps

from db_client import DbClient

client = DbClient('advertisements')

def main(req: func.HttpRequest) -> func.HttpResponse:


    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            data = client.getItems(id)
            result = dumps(data)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)