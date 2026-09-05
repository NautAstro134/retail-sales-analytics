select
    region,
    round(
        sum(quantity * unit_price * (1 - discount))::numeric,
        2
    ) as revenue
from public.sales_raw
group by region
order by revenue desc
