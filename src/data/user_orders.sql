SELECT users.name , users.id as user_id, COALESCE(SUM(amount), 0) AS total_orders -- sum simply skips 
FROM users
LEFT JOIN orders
ON user.id = orders.user_id 
GROUP BY user_id, users.name; 
