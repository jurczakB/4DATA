{{ config(materialized='view') }}

SELECT
    product_id,
    product_name,
    category,
    price::FLOAT AS price
FROM {{ ref('products') }}
