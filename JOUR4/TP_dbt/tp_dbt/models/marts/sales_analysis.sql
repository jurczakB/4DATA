{{ config(materialized='incremental', unique_key='order_id') }}

SELECT
    o.order_id,
    c.customer_name,
    c.email,
    p.product_name,
    p.category,
    o.quantity,
    o.total_amount,
    o.order_date
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_customers') }} c ON o.customer_id = c.customer_id
JOIN {{ ref('stg_products') }} p ON o.product_id = p.product_id

{% if is_incremental() %}
WHERE o.order_date > (SELECT MAX(order_date) FROM {{ this }})
{% endif %}
