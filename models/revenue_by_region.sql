select
    region,
    round(sum(revenue)::numeric, 2) as revenue
from {{ ref('stg_sales') }}
group by region
order by revenue desc
