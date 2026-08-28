import os
import json
from src.utils import normalize_product
def normalizer(base_path):
    final_data=[]
    for path in os.listdir(base_path):
        with open(os.path.join(base_path,path),"r",encoding="utf-8") as f:
            data=json.load(f)
        for i in data:
            product=normalize_product(i)
            final_data.append(product)
    with open("data/processed/products.json","w",encoding="utf-8") as f:
        json.dump(final_data,f,indent=2,ensure_ascii=False)
