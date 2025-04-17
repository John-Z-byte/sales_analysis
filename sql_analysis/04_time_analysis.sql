
-- 1. Total sales, profit, and quantity by year
SELECT 
    d."Year",
    ROUND(SUM(f."Sales"), 2) AS total_sales,
    ROUND(SUM(f."Profit"), 2) AS total_profit,
    SUM(f."Quantity") AS total_quantity
FROM fctOrders f
JOIN dimDate d ON f."Order Date" = d."Date"
GROUP BY d."Year"
ORDER BY d."Year";


-- Monthly sales trend 
SELECT 
    EXTRACT(MONTH FROM TO_DATE(f."Order Date", 'YYYY-MM-DD')) AS month,
    ROUND(SUM(f."Sales"), 2) AS total_sales
FROM fctOrders f
GROUP BY month
ORDER BY month;

