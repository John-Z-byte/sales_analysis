-- Total sales, profit margin, and quantity per product
SELECT 
    p."Product Name",
    p."Category",
    p."Sub-Category",
    SUM(f."Sales") AS total_sales,
    SUM(f."Profit") AS total_profit,
    ROUND(SUM(f."Profit") / NULLIF(SUM(f."Sales"), 0), 4) AS profit_margin,
    SUM(f."Quantity") AS total_quantity
FROM fctOrders f
JOIN dimProduct p ON f."Product Key" = p."Product Key"
GROUP BY p."Product Name", p."Category", p."Sub-Category"
ORDER BY total_sales DESC;
