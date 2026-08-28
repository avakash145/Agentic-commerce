from database import get_connection
from psycopg2.extras import Json
import pprint
def get_products():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    select product_id,raw_data from products;""")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def insert_review(product_id,review):
    conn=get_connection()
    cursor=conn.cursor()
    query='''
    insert into reviews
    (review_id,product_id,
    username,rating,
    title,review_text,
    review_date,review_url,
    reaction,is_verified,
    is_amazon_vine,variant,
    raw_data
    )
    values(
    %s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,
    %s,%s,%s
    )
    on conflict (review_id)
    do update set 
    username=excluded.username,
    rating=excluded.rating,
    title=excluded.title,
    review_text=excluded.review_text,
    review_date=excluded.review_date,
    review_url=excluded.review_url,
    reaction=excluded.reaction,
    is_verified=excluded.is_verified,
    variant=excluded.variant,
    raw_data=excluded.raw_data
    returning review_id;'''
    cursor.execute(query,(
        review.get('reviewId'),
        product_id,
        review.get('username'), 
        review.get('ratingScore'), 
        review.get('reviewTitle'), 
        review.get('reviewDescription'), 
        review.get('date'), 
        review.get('reviewUrl'), 
        review.get('reviewReaction'), 
        review.get('isVerified'), 
        review.get('isAmazonVine'), 
        review.get('variant'),
        Json(review)
    ))
    review_id=cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return review_id


def ingest_reviews():
    products=get_products()
    total=0
    for product_id,raw_data in products:
        reviews=raw_data['reviews'] or []
        for review in reviews:
            review_id=review.get('reviewId')
            if not review_id:
                continue
            insert_review(product_id,review)
            total+=1
        print(f'Product {product_id} : {len(reviews)}')
    print(f'Total reviews processed: {total}')

if __name__=="__main__":
    ingest_reviews()
