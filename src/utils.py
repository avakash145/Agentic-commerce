def normalize_product(raw):
    product={
        "identity": {
            "asin": raw.get("asin"),
            "original_asin": raw.get("originalAsin"),
            "title": raw.get("title"),
            "url": raw.get("url"),
            "brand": raw.get("brand"),
        },
        "commerce": {
            "price": raw.get("price"),
            "list_price": raw.get("listPrice"),
            "shipping_price": raw.get("shippingPrice"),
            "in_stock": raw.get("inStock"),
            "in_stock_text": raw.get("inStockText"),
            "delivery": raw.get("delivery"),
            "fastest_delivery": raw.get("fastestDelivery"),
            "return_policy": raw.get("returnPolicy"),
            "condition": raw.get("condition"),
            "offers": raw.get("offers"),
            "seller": raw.get("seller"),
        },
        "classification": {
            "breadcrumbs": raw.get("breadCrumbs"),
            "attributes": raw.get("attributes", []),
            "product_overview": raw.get("productOverview", []),
            "variant_attributes": raw.get(
                "variantAttributes", []
            ),
        },
        "content": {
            "description": raw.get("description"),
            "features": raw.get("features", []),
            "a_plus_content": raw.get("aPlusContent"),
        },
        "ratings": {
            "stars": raw.get("stars"),
            "stars_breakdown": raw.get("starsBreakdown"),
            "reviews_count": raw.get("reviewsCount"),
            "answered_questions": raw.get("answeredQuestions"),
        },

        "popularity": {
            "bestseller_ranks": raw.get("bestsellerRanks"),
            "is_amazon_choice": raw.get("isAmazonChoice"),
            "amazon_choice_text": raw.get(
                "amazonChoiceText"
            ),
        },
        "media": {
            "thumbnail": raw.get("thumbnailImage"),
            "gallery": raw.get("galleryThumbnails", []),
            "high_resolution": raw.get(
                "highResolutionImages", []
            ),
            "video_count": raw.get("videosCount", 0),
        },

        "variants": {
            "variant_asins": raw.get("variantAsins", []),
            "variant_details": raw.get(
                "variantDetails", []
            ),
        },
        "review_intelligence": raw.get(
            "aiReviewsSummary"
        ),
        "reviews": raw.get(
            "productPageReviews", []
        ),
    }
    return product