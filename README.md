# Data Engineer: Technical Test

The technical test consists of two tasks, the first is a SQL test and the second is a coding task.

You will be given up to a week to finish this test.

**When in `api`, `api-client` and `data_modelling` directories I advise creating and activating a Python virtual environment and installing requirements using `pip install -r requirements.txt`**

## SQL test

Estimated time required: 30 mins

We have a database with 2 tables. The user table has a one-to-many relationship to the orders table, and all orders must have a user, however not all users have orders.

### Question 1:

Write a SQL query to list ALL the users (including user_id and name) with the number of orders they have done including users who haven’t ordered anything yet.

**Please see `SQL/SQL_Q1.sql`**

```sql
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
```

### Question 2: 

Write a SQL query to list the users (including user_id and name) that haven’t got any orders.

**Please see `SQL/SQL_Q1.sql`**

```sql
SELECT
    user.user_id,
    user.name
FROM
    user
WHERE
    user.user_id NOT IN (SELECT DISTINCT user_id FROM orders)
```

### Question 3: 
Write a SQL query to list the users that have orders greater than £100. Include user_id, name, and the total number of orders they have done including those less than £100.

```sql
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
```

## Coding task

**Please see the `api-client` directory for full details**

Estimated time required: 1-2 hours

Using Python and any additional libraries create a client for extracting data from the API in app.py. This should be a Python interface that makes it easier for other developers and data engineers to build programs to extract data from the API and not a script to extract all the data from the API.

The API has four endpoints:

- /index: returns a welcome message

- /campaign_statistics: returns data about a marketing campaign performance, see files/campagin_statistics.json

- /campaigns.json: returns data about marketing campaigns, see campaigns.json

- /creatives.json: returns data about creatives for ads, see creatives.json

Considerations:

- The client has to send an api key in the header to authenticate

Requirements:

- The client should be able to paginate over responses

- A user of the API client should be able to select a specific page to get data from if the endpoint has multiple pages

  

## Data modelling

**Please see the `data_modelling` directory for full details**

Estimated time required: 30 mins

Design a schema from the API data which is easy to understand and optimised for running aggregations on.