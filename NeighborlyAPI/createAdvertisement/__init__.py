import azure.functions as func
import pymongo

from db_client import DbClient

client = DbClient('ads')

def main(req: func.HttpRequest) -> func.HttpResponse:

    json = req.get_json()
    
    if json:
        try:
            client.addNew(eval(json))
            return func.HttpResponse(req.get_body())
        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )
