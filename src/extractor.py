import json 
from pathlib import Path
import  logging
logger=logging.getLogger(__name__)
logger.setLevel('DEBUG')
file_handler=logging.FileHandler('logs/extractor.py')
console_handler=logging.StreamHandler()
file_handler.setLevel('DEBUG')
console_handler.setLevel('DEBUG')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
raw_path=Path("data/processed/products.json")
def extract_products():
    try:
        with open(raw_path,'r',encoding='utf-8') as f:
            products=json.load(f)
        print(f'loaded {len(products)}  raw products')
        logger.debug(f'loaded {len(products)}  raw products')
        return products
    except FileNotFoundError as e:
        logger.debug(f'file not found , error: {e}')
        raise e
    except Exception as e:
        logger.debug(f'Error has been occured')
        raise e