import logging
from bson.json_util import dumps
import azure.functions as func

from db_client import DbClient

client = DbClient('posts')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing a post delete request')

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
