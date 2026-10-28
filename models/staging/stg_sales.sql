select
    order_id,
    order_date,
    rep,
    region,
    product,
    quantity,
    unit_price,
    discount,
    quantity * unit_price * (1 - discount) as revenue
from {{ source('raw', 'sales_raw') }}
