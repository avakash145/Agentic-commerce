REQUIRED_FIELDS=[
    "asin",
    "title",
    "price",
    "brand"
]

def validate_product(product):
    missing=[]
    for field in REQUIRED_FIELDS:
        if product.get(field) in [None,""]:
            missing.append(field)
    if missing:
        return False,missing
    return True, []