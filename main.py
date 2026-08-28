import json
from src.data_normalizer import normalizer
import os 
base_path='data/raw/'
normalizer(base_path)
from src.extractor import extract_products
from src.transformer import transform_product
from src.validator import validate_product
from src.loader import load_product


raw_products = extract_products()

for i in range(len(raw_products)):
    raw_product=raw_products[i]
    product = transform_product(raw_product)
    valid, missing = validate_product(product)
    if valid:
        print(product.get('in_stock'))
        product_id = load_product(product)
        print("Inserted product ID:", product_id)
    