select
    rep as salesperson,
    round(
        sum(quantity * unit_price * (1 - discount))::numeric,
        2
    ) as revenue
from public.sales_raw
group by rep
order by revenue desc
