import azure.functions as func
from bson.json_util import dumps

from db_client import DbClient

client = DbClient('ads')

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        data = client.getItems()
        result = dumps(data)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

