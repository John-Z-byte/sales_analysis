-- Customer value distribution per segment
SELECT 
    s."Customer Segment",
    f."Customer Value",
    COUNT(DISTINCT f."Customer Key") AS customer_count
FROM fctOrders f
JOIN dimCustomerSegment s ON f."Segment Key" = s."Segment Key"
GROUP BY s."Customer Segment", f."Customer Value"
ORDER BY s."Customer Segment", customer_count DESC;

