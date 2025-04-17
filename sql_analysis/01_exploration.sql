-- Total sales, profit, and quantity across all orders
SELECT 
    ROUND(SUM("Sales"), 2) AS total_sales,
    ROUND(SUM("Profit"), 2) AS total_profit,
    SUM("Quantity") AS total_quantity
FROM fctOrders;
