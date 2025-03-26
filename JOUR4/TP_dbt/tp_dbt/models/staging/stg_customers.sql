{{ config(materialized='view') }}

SELECT
    customer_id,
    customer_name,
    LOWER(email) AS email,
    signup_date::DATE AS signup_date
FROM {{ ref('customers') }}
