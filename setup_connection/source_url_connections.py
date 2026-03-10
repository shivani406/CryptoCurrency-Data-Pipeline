import websockets
import logging
from logging_setup import init_logging


# setup logging for the websocket connection setup process
init_logging()
logger = logging.getLogger(__name__)

# define 4 callback fucntions for the websocket connection setup process - on_open, on_message, on_error and on_close

def on_open(ws):
    logger.info("Websocket connection opened")


def on_message(ws, message):  

    logger.info(f"Received message: {message}")
    # print the incoming message from the websocket connection for now
    print(message)

    # processing will be minimal just check for null/empty messages
    if not message:
        logger.warning("Received empty message")
        return

    # Send Data to kafka 
   # producer.produce('raw-trades', value=message)
    
    #=== add occasional debug logs to check the frequency of incoming messages and the size of the messages 


def on_error(ws, error):
    logger.error(f"Websocket error: {error}")
    #=== further attempt to reconnect can be implemented here in case of an error in the websocket connection, but for now we will just log the error and move on

def on_close(ws):
    logger.info("Websocket connection closed")


def setup_websocket_connection(source_url , source_name):
    # Save logs whenever a websocket_connection is setup
    logger.info(f"Setting up websocket connection to {source_url} for source {source_name}")

    ws = websockets.WebSocketApp(
        source_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws.run_forever()
