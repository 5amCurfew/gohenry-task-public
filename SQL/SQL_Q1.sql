WITH order_count AS (

    SELECT
        user_id,
        COUNT(DISTINCT order_id)
    FROM
        order
    GROUP BY
        1

)

SELECT
    user.user_id,
    user.name,
    COALESCE(order_count, 0) as order_count
FROM
    user
    LEFT JOIN order_count ON order_count.user_id = user.user_id
