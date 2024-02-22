import os
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

# connection_string = os.getenv("hubconstr")
connection_string = 'Endpoint=sb://neighbourlyappevent.servicebus.windows.net/;SharedAccessKeyName=access;SharedAccessKey=M6kbQ4FsaZ2OHspfcz6OQjBLl09z/iQUp+AEhOZN0A0=;EntityPath=neighbour'
hub_name = "neighbour"

class EventHubMessages:
	async def send_message(self, event : str):
		# Create a producer client to send messages to the event hub.
		# Specify a connection string to your event hubs namespace and
		# the event hub name.
		producer = EventHubProducerClient.from_connection_string(
			conn_str=connection_string, eventhub_name=hub_name
		)
		async with producer:
			# Send the batch of events to the event hub.
			eventData = EventData(event)
			await producer.send_event(eventData)