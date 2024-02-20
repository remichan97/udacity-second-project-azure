import json
import logging
import azure.functions as func


def main(event: func.EventGridEvent):

    logging.info('Function triggered to process a message: ', event.get_json())
    logging.info('  EnqueuedTimeUtc =', event.event_time)
    logging.info('  Version =', event.data_version)
    logging.info('  Type =', event.event_type)

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })


    logging.info('Python EventGrid trigger processed an event: %s', result)