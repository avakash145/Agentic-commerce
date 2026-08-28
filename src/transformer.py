def transform_product(raw):

    identity = raw.get("identity") or {}
    commerce = raw.get("commerce") or {}
    ratings = raw.get("ratings") or {}
    classification = raw.get("classification") or {}
    content = raw.get("content") or {}
    popularity = raw.get("popularity") or {}
    media = raw.get("media") or {}

    price = commerce.get("price") or {}
    list_price = commerce.get("list_price") or {}
    shipping_price = commerce.get("shipping_price") or {}

    return {

        "asin": identity.get("asin"),
        "original_asin": identity.get("original_asin"),
        "title": identity.get("title"),
        "brand": identity.get("brand"),
        "url": identity.get("url"),

        "price": price.get("value"),
        "currency": price.get("currency"),

        "list_price": list_price.get("value"),
        "shipping_price": shipping_price.get("value"),

        "stars": ratings.get("stars"),
        "reviews_count": ratings.get("reviews_count"),
        "answered_questions": ratings.get("answered_questions"),

        "breadcrumbs": classification.get("breadcrumbs"),
        "description": content.get("description"),
        "features": content.get("features") or [],

        "attributes": classification.get("attributes") or [],
        "product_overview": classification.get(
            "product_overview"
        ) or [],

        "in_stock": commerce.get("in_stock"),
        "in_stock_text": commerce.get("in_stock_text"),

        "delivery": commerce.get("delivery"),
        "fastest_delivery": commerce.get("fastest_delivery"),

        "condition": commerce.get("condition"),
        "return_policy": commerce.get("return_policy"),

        "is_amazon_choice": popularity.get(
            "is_amazon_choice"
        ),

        "amazon_choice_text": popularity.get(
            "amazon_choice_text"
        ),

        "bestseller_ranks": popularity.get(
            "bestseller_ranks"
        ),

        "video_count": media.get("video_count", 0),

        "raw_data": raw
    }
def transform_reviews(raw):

    reviews = []

    for review in raw.get("productPageReviews", []):

        reviews.append({

            "review_id": review.get("reviewId"),

            "asin": raw.get("asin"),

            "username": review.get("username"),

            "rating": review.get("ratingScore"),

            "title": review.get("reviewTitle"),

            "review_text": review.get("reviewDescription"),

            "review_date": review.get("date"),

            "verified": review.get("isVerified"),

            "amazon_vine": review.get("isAmazonVine"),

            "variant": review.get("variant"),

            "reaction": review.get("reviewReaction"),

            "images": review.get("reviewImages", []),

            "raw_data": review
        })

    return reviews
def transform_media(raw):

    media = []

    asin = raw["asin"]

    if raw.get("thumbnailImage"):

        media.append({
            "asin": asin,
            "review_id": None,
            "media_type": "thumbnail",
            "url": raw["thumbnailImage"]
        })

    for image in raw.get("galleryThumbnails", []):

        media.append({
            "asin": asin,
            "review_id": None,
            "media_type": "gallery",
            "url": image
        })

    for image in raw.get("highResolutionImages", []):

        media.append({
            "asin": asin,
            "review_id": None,
            "media_type": "high_resolution",
            "url": image
        })

    aplus = raw.get("aPlusContent")

    if aplus:

        for image in aplus.get("rawImages", []):

            media.append({
                "asin": asin,
                "review_id": None,
                "media_type": "aplus_image",
                "url": image["url"]
            })

    for review in raw.get("productPageReviews", []):

        for image in review.get("reviewImages", []):

            media.append({

                "asin": asin,

                "review_id": review.get("reviewId"),

                "media_type": "review_image",

                "url": image
            })

    return media