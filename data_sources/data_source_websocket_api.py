import asyncio
import websockets
import json
import logging
from logging_setup import init_logging
from setup_connection.source_url_connections import setup_websocket_connection

init_logging()
logger = logging.getLogger(__name__)

# Websocket Exchanges

exchanges = {
    "binance": {"wss://ws-api.binance.com:443/ws-api/v3"
    }
    # Add more exchanges and their websocket URLs here
}


if __name__ =="__main__":
    for source_name, source_url in exchanges.items():
        # call the function to establish connection in another file
        setup_websocket_connection(source_url , source_name)