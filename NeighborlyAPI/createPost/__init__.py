import logging

import azure.functions as func

from db_client import DbClient

client = DbClient('posts')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing add post request')

    json = req.get_json()
    
    if json:
        try:
            client.addNew(json)
            return func.HttpResponse(req.get_body())
        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )
