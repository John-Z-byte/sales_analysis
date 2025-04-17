-- Sales and profit by sales team
SELECT 
    t."Sales Team",
    ROUND(SUM(f."Sales"), 2) AS total_sales,
    ROUND(SUM(f."Profit"), 2) AS total_profit
FROM fctOrders f
JOIN dimSalesTeam t ON f."Sales Team Key" = t."Sales Team Key"
GROUP BY t."Sales Team"
ORDER BY total_sales DESC;

-- Sales and profit by sales rep
SELECT 
    t."Sales Rep",
    ROUND(SUM(f."Sales"), 2) AS total_sales,
    ROUND(SUM(f."Profit"), 2) AS total_profit,
    COUNT(DISTINCT f."Order ID") AS total_orders
FROM fctOrders f
JOIN dimSalesTeam t ON f."Sales Team Key" = t."Sales Team Key"
GROUP BY t."Sales Rep"
ORDER BY total_sales DESC;

-- Total orders handled per sales team
SELECT 
    t."Sales Team",
    COUNT(DISTINCT f."Order ID") AS total_orders
FROM fctOrders f
JOIN dimSalesTeam t ON f."Sales Team Key" = t."Sales Team Key"
GROUP BY t."Sales Team"
ORDER BY total_orders DESC;

-- Total sales grouped by sales team manager
SELECT 
    t."Sales Team Manager",
    ROUND(SUM(f."Sales"), 2) AS total_sales
FROM fctOrders f
JOIN dimSalesTeam t ON f."Sales Team Key" = t."Sales Team Key"
GROUP BY t."Sales Team Manager"
ORDER BY total_sales DESC;


