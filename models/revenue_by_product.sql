select
    product,
    round(sum(revenue)::numeric, 2) as revenue
from {{ ref('stg_sales') }}
group by product
order by revenue desc
