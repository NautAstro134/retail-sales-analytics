select
    date_trunc('month', order_date)::date as month,
    round(sum(revenue)::numeric, 2) as revenue
from {{ ref('stg_sales') }}
group by 1
order by 1
