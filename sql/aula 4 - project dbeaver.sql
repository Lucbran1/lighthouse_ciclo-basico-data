-- Active: 1772152469331@@127.0.0.1@3306

-- 3 CATEGORIAS QUE MAIS GERARAM RECEITA TOTAL
SELECT
    c.CategoryName,
    SUM(od.UnitPrice * od.Quantity) AS receita_total
FROM Category c
INNER JOIN Product p
    ON c.Id = p.CategoryId
INNER JOIN OrderDetail od
    ON p.Id = od.ProductId
GROUP BY c.CategoryName
ORDER BY receita_total DESC
LIMIT 3;