# Retail Sales Analytics

End-to-end retail sales analytics project using PostgreSQL, dbt, SQL, and Metabase.

## Dashboard

The Metabase dashboard includes total revenue, total orders, items sold, revenue by product, region, and salesperson, a monthly revenue trend, and interactive filters.

### Dashboard — Top

![Retail Sales Dashboard Top](dashboard-top.png)

### Dashboard — Bottom

![Retail Sales Dashboard Bottom](dashboard-bottom.png)

## Published Business Results

These validated results come from the original 1,000-order synthetic project dataset used for the dashboard:

- Total Revenue: $6,898,908.67
- Total Orders: 1,000
- Items Sold: 10,373
- Top Product: Desk — $1,021,571.12
- Top Salesperson: Carlos — $1,418,990.97
- Top Region: North — $1,779,969.45

## Reproduce the Pipeline

The original dashboard dataset is synthetic but is not redistributed in this repository. To make the pipeline runnable without private or missing files, the repository includes a deterministic demo-data generator with the same schema.

> The generated demo data validates the engineering workflow. Its totals will differ from the published dashboard results above.

### Requirements

- Python 3.10+
- PostgreSQL
- dbt-postgres

### 1. Install the Python/dbt dependency

```bash
python -m pip install -r requirements.txt
```

### 2. Generate 1,000 demo orders

```bash
python scripts/generate_sample_data.py
```

This creates `data/sales_demo.csv`.

### 3. Create and load the PostgreSQL table

Create an empty database named `retail_sales`, then run:

```bash
psql -d retail_sales -f sql/01_create_sales_raw.sql
psql -d retail_sales -c "\copy public.sales_raw FROM 'data/sales_demo.csv' WITH (FORMAT csv, HEADER true)"
```

### 4. Configure dbt

Copy `profiles.yml.example` to `~/.dbt/profiles.yml`. Set these environment variables for your PostgreSQL instance:

- `DBT_HOST`
- `DBT_PORT`
- `DBT_USER`
- `DBT_PASSWORD`
- `DBT_DATABASE`

### 5. Build and test

```bash
dbt debug
dbt build
```

The staging model reads the declared `raw.sales_raw` source. Every downstream model uses `ref('stg_sales')`, so dbt manages dependencies consistently.

## Data Pipeline

Synthetic CSV → PostgreSQL raw table → dbt staging model → analytics models → Metabase dashboard → business recommendations

## Business Findings

Desk and Laptop are the strongest products by revenue, each generating approximately $1 million.

Carlos is the strongest salesperson, generating approximately $1.42 million in revenue.

Regional performance is balanced. North leads at about $1.78 million, while all four regions generate between approximately $1.67 million and $1.78 million.

Monthly revenue fluctuates considerably, making product, salesperson, region, and date filters useful for investigating changes in performance.

## Recommended Actions

- Prioritize Desk and Laptop inventory and promotions; together they generate $2.03 million in revenue.
- Use Carlos as a sales benchmark; his $1.42 million exceeds the lowest salesperson by about $459,000.
- Test campaigns in East; North generates about $106,838 more revenue.

## Data Validation

PostgreSQL and dbt checks confirmed 1,000 orders, 10,373 items sold, and $6,898,908.67 in revenue for the original dashboard dataset.

dbt tests cover unique and non-null order IDs, required fields, and accepted values for region, product, salesperson, and discount.

## Technology

- PostgreSQL
- SQL
- dbt
- Metabase
- Python
- Git
- GitHub

## Client Use Case

This workflow can be adapted for a small business with sales data in Excel, CSV files, or an existing database. The deliverable can include cleaned data, repeatable transformations, business analysis, an interactive dashboard, and a short findings report.
