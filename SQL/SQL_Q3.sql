SELECT
    user.id,
    user.name,
    COUNT(orders.id) as order_count,
    COUNT(CASE WHEN orders.transaction_amount >= 100 THEN orders.id END) as large_order_count
FROM
    user
    INNER JOIN orders ON orders.user_id = users.user_id
GROUP BY
    1,2
HAVING
    large_order_count > 0
