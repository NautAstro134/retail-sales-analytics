select
    rep as salesperson,
    round(sum(revenue)::numeric, 2) as revenue
from {{ ref('stg_sales') }}
group by rep
order by revenue desc
