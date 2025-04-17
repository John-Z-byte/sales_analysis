-- Sales and profit by region
SELECT 
    l."Region",
    ROUND(SUM(f."Sales"), 2) AS total_sales,
    ROUND(SUM(f."Profit"), 2) AS total_profit
FROM fctOrders f
JOIN dimLocation l ON f."Location Key" = l."Location Key"
GROUP BY l."Region"
ORDER BY total_sales DESC;

-- Top 10 cities by total sales
SELECT 
    l."City",
    ROUND(SUM(f."Sales"), 2) AS total_sales
FROM fctOrders f
JOIN dimLocation l ON f."Location Key" = l."Location Key"
GROUP BY l."City"
ORDER BY total_sales DESC
LIMIT 10;

-- Most profitable regions
SELECT 
    l."Region",
    ROUND(SUM(f."Profit"), 2) AS total_profit
FROM fctOrders f
JOIN dimLocation l ON f."Location Key" = l."Location Key"
GROUP BY l."Region"
ORDER BY total_profit DESC
LIMIT 3;

-- Sales by state
SELECT 
    l."State",
    ROUND(SUM(f."Sales"), 2) AS total_sales
FROM fctOrders f
JOIN dimLocation l ON f."Location Key" = l."Location Key"
GROUP BY l."State"
ORDER BY total_sales DESC;
