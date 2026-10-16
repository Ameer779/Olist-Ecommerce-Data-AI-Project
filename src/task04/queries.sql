
-- Task 04: SQL Data Analysis
-- Dataset: Olist Brazilian E-Commerce

-- Query 1: View sample customer records (SELECT)
SELECT *
FROM customers
LIMIT 10;


-- Query 2: Filter delivered orders (WHERE)
SELECT order_id, customer_id, order_status
FROM orders
WHERE order_status = 'delivered'
LIMIT 20;


-- Query 3: Most common order statuses (GROUP BY)
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;


-- Query 4: Payment methods and total payments (aggregate)
SELECT
    payment_type,
    COUNT(*) AS payment_records,
    ROUND(SUM(payment_value), 2) AS total_payment
FROM order_payments
GROUP BY payment_type
ORDER BY total_payment DESC;


-- Query 5: Join orders with customers
SELECT
    o.order_id,
    o.order_status,
    c.customer_city,
    c.customer_state
FROM orders AS o
JOIN customers AS c
    ON o.customer_id = c.customer_id
LIMIT 20;


-- Query 6: Top product categories by number of products
SELECT
    COALESCE(
        t.product_category_name_english,
        p.product_category_name,
        'Unknown'
    ) AS product_category,
    COUNT(*) AS total_products
FROM products AS p
LEFT JOIN category_translation AS t
    ON p.product_category_name = t.product_category_name
GROUP BY product_category
ORDER BY total_products DESC
LIMIT 10;


-- Query 7: Average review score
SELECT
    ROUND(AVG(review_score), 2) AS average_review_score,
    COUNT(*) AS total_reviews
FROM order_reviews;


-- Query 8: Orders by customer state
SELECT
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC
LIMIT 10;
