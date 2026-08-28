import json
import psycopg2
from psycopg2.extras import Json
from pathlib import Path
# processed =Path("data/processed")
# processed.mkdir(exist_ok=True)
# def save_json(name, data):
#     path=processed/f"{name}.json"
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(data,f,indent=2,ensure_ascii=False)

#     print(f"Saved {path}")


from src.database import get_connection


def load_product(product):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO products (
            asin,
            original_asin,
            title,
            brand,
            url,
            price,
            currency,
            list_price,
            shipping_price,
            in_stock,
            in_stock_text,
            stars,
            reviews_count,
            answered_questions,
            breadcrumbs,
            description,
            delivery,
            fastest_delivery,
            return_policy,
            condition,
            is_amazon_choice,   
            amazon_choice_text,
            video_count,
            raw_data
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        ON CONFLICT (asin)
        DO UPDATE SET
            title = EXCLUDED.title,
            price = EXCLUDED.price,
            in_stock = EXCLUDED.in_stock,
            stars = EXCLUDED.stars,
            reviews_count = EXCLUDED.reviews_count,
            updated_at = CURRENT_TIMESTAMP
        RETURNING product_id;
    """

    cursor.execute(query, (
        product["asin"],
        product["original_asin"],
        product["title"],
        product["brand"],
        product["url"],
        product["price"],
        product["currency"],
        product["list_price"],
        product["shipping_price"],
        product["in_stock"],
        product["in_stock_text"],
        product["stars"],
        product["reviews_count"],
        product["answered_questions"],
        product["breadcrumbs"],
        product["description"],
        product["delivery"],
        product["fastest_delivery"],
        product["return_policy"],
        product["condition"],
        product["is_amazon_choice"],
        product["amazon_choice_text"],
        product["video_count"],
        Json(product["raw_data"])
    ))
    product_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return product_id