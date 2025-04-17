-- Top-selling product per month using
WITH monthly_sales AS (
    SELECT 
        TO_DATE(f."Order Date", 'YYYY-MM-DD') AS order_date,
        p."Product Name",
        EXTRACT(YEAR FROM TO_DATE(f."Order Date", 'YYYY-MM-DD')) AS year,
        EXTRACT(MONTH FROM TO_DATE(f."Order Date", 'YYYY-MM-DD')) AS month,
        SUM(f."Sales") AS total_sales,
        ROW_NUMBER() OVER (
            PARTITION BY EXTRACT(YEAR FROM TO_DATE(f."Order Date", 'YYYY-MM-DD')), 
                         EXTRACT(MONTH FROM TO_DATE(f."Order Date", 'YYYY-MM-DD'))
            ORDER BY SUM(f."Sales") DESC
        ) AS rank
    FROM fctOrders f
    JOIN dimProduct p ON f."Product Key" = p."Product Key"
    GROUP BY year, month, p."Product Name", order_date
)
SELECT * FROM monthly_sales WHERE rank = 1;

-- Running profit per customer across time
SELECT 
    c."Customer Name",
    TO_DATE(f."Order Date", 'YYYY-MM-DD') AS order_date,
    f."Profit",
    SUM(f."Profit") OVER (
        PARTITION BY c."Customer Name"
        ORDER BY TO_DATE(f."Order Date", 'YYYY-MM-DD')
    ) AS cumulative_profit
FROM fctOrders f
JOIN dimCustomer c ON f."Customer Key" = c."Customer Key"
ORDER BY c."Customer Name", order_date;

-- YoY Sales Growth by Category
WITH category_sales AS (
    SELECT 
        EXTRACT(YEAR FROM TO_DATE(f."Order Date", 'YYYY-MM-DD')) AS year,
        p."Category",
        SUM(f."Sales") AS total_sales
    FROM fctOrders f
    JOIN dimProduct p ON f."Product Key" = p."Product Key"
    GROUP BY year, p."Category"
),
yoy_growth AS (
    SELECT 
        cs1."Category",
        cs1."year",
        cs1.total_sales,
        LAG(cs1.total_sales) OVER (PARTITION BY cs1."Category" ORDER BY cs1."year") AS prev_year_sales,
        ROUND(((cs1.total_sales - LAG(cs1.total_sales) OVER (PARTITION BY cs1."Category" ORDER BY cs1."year")) /
               NULLIF(LAG(cs1.total_sales) OVER (PARTITION BY cs1."Category" ORDER BY cs1."year"), 0)) * 100, 2) AS yoy_growth_percent
    FROM category_sales cs1
)
SELECT * FROM yoy_growth
WHERE prev_year_sales IS NOT NULL
ORDER BY "Category", "year";
