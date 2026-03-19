import asyncio
import json
import aiokafka
import logging
from logging_setup import init_logging
from setup_connection.source_url_connections import setup_websocket_connection


init_logging()
logger = logging.getLogger(__name__)

# Create one single kafka producer that can be used across all websocket connections 

async def main():
    shared_producer = aiokafka.AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        client_id='crypto-shared-producer',
        enable_idempotence=True,
        value_serializer = lambda v:json.dumps(v).encode('utf-8')
        #=== can add compression technique here to optimize the data transfer
    )
    await shared_producer.start()


    # Websocket Exchanges

    exchanges = {
        "binance": {"wss://ws-api.binance.com:443/ws-api/v3"
        }
        # Add more exchanges and their websocket URLs here
    }

    for source_name, source_websocket_url in exchanges.items():

        try:
            asyncio.create_task(setup_websocket_connection(source_websocket_url , source_name, producer = shared_producer))
        except Exception as e:
            logger.error(f"Error occurred while setting up websocket connection for {source_name}: {e}")


if __name__ =="__main__":
    asyncio.run(main())


