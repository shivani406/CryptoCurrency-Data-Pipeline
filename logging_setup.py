import logging

# setup logging for the entire project

def init_logging():
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(message)s',
        force=True 
        )