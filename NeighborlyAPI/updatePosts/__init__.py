import logging

import azure.functions as func

from db_client import DbClient

client = DbClient('posts')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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
