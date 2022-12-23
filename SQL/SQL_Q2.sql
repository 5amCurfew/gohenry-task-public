SELECT
    user.user_id,
    user.name
FROM
    user
WHERE
    user.user_id NOT IN (SELECT DISTINCT user_id FROM orders)