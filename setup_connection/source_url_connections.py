import websockets    
import logging
from logging_setup import init_logging


# setup logging for the websocket connection setup process
init_logging()
logger = logging.getLogger(__name__)


def on_open(ws):
    logger.info("Websocket connection opened")

def on_message(ws, message):
    logger.info(f"Received message: {message}")
    # print the incoming message from the websocket connection for now



def on_error(ws, error):
    logger.error(f"Websocket error: {error}")

def on_close(ws):
    logger.info("Websocket connection closed")


def setup_websocket_connection(source_url):
    # Save logs whenever a websocket_connection is setup
    logger.info(f"Setting up websocket connection to {source_url}")
    #  add the actual code to establish the websocket connection

    ws = websockets.WebSocketApp(source_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    
    ws.run_forever()
    
