import asyncio
import websockets
import json
import logging

#====Websocket Exchanges====

exchanges = {
    "binance": {"wss://ws-api.binance.com:443/ws-api/v3"
    
    }
    # Add more exchanges and their websocket URLs here
}

