--#1 Detects customers who had transactions within 5 minutes of their previous one
WITH timed_transactions AS (
    SELECT 
        customer_id,
        transaction_id,
        merchant_id,
        amount,
        transaction_time,
        LAG(transaction_time) OVER (
            PARTITION BY customer_id 
            ORDER BY transaction_time
        ) AS prev_transaction_time
    FROM master_dataset
)
SELECT 
    customer_id,
    transaction_id,
    merchant_id,
    amount,
    transaction_time,
    prev_transaction_time,
    (transaction_time - prev_transaction_time) AS time_difference
FROM timed_transactions
WHERE prev_transaction_time IS NOT NULL 
  AND transaction_time - prev_transaction_time <= INTERVAL '5 minutes'
ORDER BY time_difference ASC;

-- -- #2 Calculates what % of their annual income (as a proxy for credit line capacity) they spend per month
WITH monthly_customer_spend AS (
    SELECT 
        customer_id,
        annual_income,
        DATE_TRUNC('month', transaction_time) AS spend_month,
        SUM(amount) AS total_month_spend
    FROM master_dataset
    GROUP BY customer_id, annual_income, DATE_TRUNC('month', transaction_time)
)
SELECT 
    customer_id,
    spend_month,
    total_month_spend,
    annual_income,
    ROUND(((total_month_spend / (annual_income / 12.0)) * 100)::numeric, 2) AS monthly_income_utilization_pct
FROM monthly_customer_spend
WHERE annual_income > 0
ORDER BY monthly_income_utilization_pct DESC;

-- --#3 Finds 'Premium' or 'Upper' income customers who haven't made a transaction in the last 30 days
WITH customer_last_spend AS (
    SELECT 
        customer_id,
        annual_income,
        MAX(transaction_time) AS last_transaction_date,
        (SELECT MAX(transaction_time) FROM master_dataset) AS dataset_current_date
    FROM master_dataset
    GROUP BY customer_id, annual_income
)
SELECT 
    customer_id,
    annual_income,
    last_transaction_date,
    EXTRACT(DAY FROM (dataset_current_date - last_transaction_date)) AS days_since_last_spend
FROM customer_last_spend
WHERE annual_income >= 1000000 -- Upper & Premium bands from your setup
  AND last_transaction_date < (SELECT MAX(transaction_time) FROM master_dataset) - INTERVAL '30 days'
ORDER BY days_since_last_spend DESC;

-- #4 Ranks merchants by the amount of money spent at them strictly by "Premium" income earners
WITH premium_spenders AS (
    SELECT 
        merchant_id,
        SUM(amount) AS premium_spend_amount,
        COUNT(DISTINCT customer_id) AS unique_premium_customers
    FROM master_dataset
    WHERE annual_income >= 2000000 -- Premium tier definition
    GROUP BY merchant_id
)
SELECT 
    merchant_id,
    ROUND(premium_spend_amount::numeric, 2) AS total_premium_revenue,
    unique_premium_customers,
    DENSE_RANK() OVER (ORDER BY premium_spend_amount DESC) AS merchant_rank
FROM premium_spenders
ORDER BY total_premium_revenue DESC
LIMIT 10;


-- #5 Ranks merchants by the amount of money spent at them strictly by "Premium" income earners
WITH premium_spenders AS (
    SELECT 
        merchant_id,
        SUM(amount) AS premium_spend_amount,
        COUNT(DISTINCT customer_id) AS unique_premium_customers
    FROM master_dataset
    WHERE annual_income >= 2000000 -- Premium tier definition
    GROUP BY merchant_id
)
SELECT 
    merchant_id,
    ROUND(premium_spend_amount::numeric, 2) AS total_premium_revenue,
    unique_premium_customers,
    DENSE_RANK() OVER (ORDER BY premium_spend_amount DESC) AS merchant_rank
FROM premium_spenders
ORDER BY total_premium_revenue DESC
LIMIT 10;