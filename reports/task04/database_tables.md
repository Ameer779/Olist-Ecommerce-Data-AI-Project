# Task 04: Database Tables Report

Database: Olist Brazilian E-Commerce (SQLite)

| Table | Rows | Columns |
|---|---:|---:|
| category_translation | 71 | 2 |

### category_translation

Columns: product_category_name, product_category_name_english
| customers | 99,441 | 5 |

### customers

Columns: customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state
| geolocation | 738,332 | 5 |

### geolocation

Columns: geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state
| order_items | 112,650 | 7 |

### order_items

Columns: order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value
| order_payments | 103,886 | 5 |

### order_payments

Columns: order_id, payment_sequential, payment_type, payment_installments, payment_value
| order_reviews | 99,224 | 7 |

### order_reviews

Columns: review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp
| orders | 99,441 | 8 |

### orders

Columns: order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date
| products | 32,951 | 9 |

### products

Columns: product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm
| sellers | 3,095 | 4 |

### sellers

Columns: seller_id, seller_zip_code_prefix, seller_city, seller_state
