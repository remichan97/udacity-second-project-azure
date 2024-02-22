import os
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

# Adapted from examples from https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/eventhub/azure-eventhub/samples/sync_samples/send.py

connection_string = str(os.getenv("hubconstr"))
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