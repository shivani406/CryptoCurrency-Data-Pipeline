import websockets
import logging_setup
import asyncio
import json
import aiokafka
from websockets.exceptions import ConnectionClosed, WebSocketException

import logging
from logging_setup import init_logging


# setup logging for the websocket connection setup process
init_logging()
logger = logging.getLogger(__name__)







def on_message(ws, message):  

    logger.info(f"Received message: {message}")
    # print the incoming message from the websocket connection for now
    print(message)

    # processing will be minimal just check for null/empty messages
    if not message:
        logger.warning("Received empty message")
        return
    
    #=== add occasional debug logs to check the frequency of incoming messages and the size of the messages 










# 4 way callback function is not used for websockets 
async def setup_websocket_connection(source_websocket_url , source_name):
    """ 
    Establish a persistent WebSocket connection to a data source,
    receive messages, and forward them to a Kafka topic.

    Args:
        source_websocket_url: The WebSocket endpoint URL (e.g., wss://stream.binance.com/...)
        source_name:            A human‑readable identifier for logging (e.g., "binance").
        kafka_topic:            Kafka topic to which raw messages will be sent.
        kafka_bootstrap_servers: Kafka broker address(es).
        reconnect_delay:        Seconds to wait before attempting a reconnect after a failure.

    """

    logger.info(f"Setting up websocket connection to {source_websocket_url} for source {source_name}")
    try:
        async with websockets.connect( source_websocket_url, ping_interval= 20, ping_timeout= 10, max_queue= 1024, user_agent_header= "crypto-pipeline/1.0") as websocket : 
        
            async for raw_mesaage in websocket:
                if :
                    
                    # check for empty msg/ not null msg, if msg is not null then log - stating that we received empty msg from the websocket
                    # Send Data to kafka if it is not null

                else:
                    #log - stating that we received empty msg from the websocket
            
    
    except:

        logger.error(f"Error fetching data from {source_websocket_url} from source {source_name}")
        #=== further attempt to reconnect can be implemented here in case of an error in the websocket connection, but for now we will just log the error and move on


    
