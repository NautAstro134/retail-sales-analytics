DROP TABLE IF EXISTS public.sales_raw;

CREATE TABLE public.sales_raw (
    order_id TEXT PRIMARY KEY,
    order_date DATE NOT NULL,
    rep TEXT NOT NULL,
    region TEXT NOT NULL,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL CHECK (unit_price >= 0),
    discount NUMERIC(4, 2) NOT NULL CHECK (discount BETWEEN 0 AND 1)
);
