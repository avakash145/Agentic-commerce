import json
from database import get_connection

def get_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT product_id,asin,raw_data FROM products;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def extract_images(product_id, raw_data):
    media=[]
    media_data=raw_data.get("media") or {}
    thumbnail=media_data.get("thumbnail")
    if thumbnail:
        media.append({
            "product_id":product_id,
            "review_id":None,
            "media_type":"product_thumbnail",
            "url":thumbnail,
            "source":"junglee"
        })

    for url in media_data.get("gallery") or []:
        media.append({
            "product_id":product_id,
            "review_id":None,
            "media_type":"product_gallery",
            "url":url,
            "source":"junglee"
        })
    for url in media_data.get("high_resolution") or []:
        media.append({
            "product_id":product_id,
            "review_id":None,
            "media_type":"product_high_resolution",
            "url":url,
            "source":"junglee"
        })
    return media
def insert_media(media):
    conn=get_connection()
    cursor=conn.cursor()
    query="""
        INSERT INTO media (product_id,review_id,media_type,url,source)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (product_id,review_id,media_type,url)
        DO NOTHING;
    """
    cursor.execute(
        query,
        (
            media["product_id"],
            media["review_id"],
            media["media_type"],
            media["url"],
            media["source"]
        )
    )
    conn.commit()
    cursor.close()
    conn.close()

def ingest_images():
    products=get_products()
    total_images=0
    for product_id,asin,raw_data in products:
        images=extract_images(product_id,raw_data)
        for image in images:
            insert_media(image)
        total_images+=len(images)
        print(f"{asin}:{len(images)} images")
    print(f"\nTotal images processed: {total_images}")

if __name__ == "__main__":
    ingest_images()
