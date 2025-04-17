-- Average discount by product category
SELECT 
    p."Category",
    ROUND(AVG(f."Discount"), 4) AS avg_discount
FROM fctOrders f
JOIN dimProduct p ON f."Product Key" = p."Product Key"
GROUP BY p."Category"
ORDER BY avg_discount DESC;


-- Average profit margin by category
SELECT 
    p."Category",
    ROUND(SUM(f."Profit") / NULLIF(SUM(f."Sales"), 0), 4) AS avg_margin
FROM fctOrders f
JOIN dimProduct p ON f."Product Key" = p."Product Key"
GROUP BY p."Category"
ORDER BY avg_margin DESC;

-- Products with high discount and low total profit
SELECT 
    p."Product Name",
    ROUND(AVG(f."Discount"), 2) AS avg_discount,
    ROUND(SUM(f."Profit"), 2) AS total_profit
FROM fctOrders f
JOIN dimProduct p ON f."Product Key" = p."Product Key"
GROUP BY p."Product Name"
HAVING AVG(f."Discount") > 0.2 AND SUM(f."Profit") < 0
ORDER BY avg_discount DESC;

-- Correlation insight: are we losing money with big discounts?
SELECT
    ROUND(AVG(f."Discount"), 4) AS avg_discount,
    ROUND(AVG(f."Profit"), 4) AS avg_profit,
    ROUND(AVG(f."Sales"), 4) AS avg_sales
FROM fctOrders f;
