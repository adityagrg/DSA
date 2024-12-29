# Write your MySQL query statement below

SELECT 
    Sales.product_id, 
    Product.product_name
FROM 
    Sales
JOIN 
    Product ON Sales.product_id = Product.product_id
WHERE 
    Sales.product_id NOT IN (
        -- Subquery to exclude products sold outside the first quarter of 2019
        SELECT product_id 
        FROM Sales 
        WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
    )
    AND Sales.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY 
    Sales.product_id, Product.product_name;