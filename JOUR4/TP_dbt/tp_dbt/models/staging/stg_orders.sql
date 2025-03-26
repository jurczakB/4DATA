{{ config(materialized='view') }}

SELECT
    order_id,
    customer_id,
    product_id,
    quantity,
    total_amount::FLOAT AS total_amount,
    order_date::TIMESTAMP AS order_date
FROM {{ ref('orders') }}
