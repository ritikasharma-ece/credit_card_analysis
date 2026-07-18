-- #1 Find occupations whose total spending is greater than the average spending across all occupations.
Select occupation , round(sum(amount)::numeric,2) as total_spending from master_dataset
group by occupation having round(sum(amount)::numeric,2) > (select avg(amount) from master_dataset) 
order by total_spending desc;

-- #2 Find customers who own more than one card.
select customer_id from master_dataset 
group by customer_id having count(distinct card_type)>1
order by customer_id asc;

-- #3 Customer Spending Rank
SELECT
    customer_id,
    round(SUM(amount)::numeric) as total_spending,

    RANK() OVER
    (
        ORDER BY SUM(amount) DESC
    ) rnk,

    DENSE_RANK() OVER
    (
        ORDER BY SUM(amount) DESC
    ) dense_rnk,

    ROW_NUMBER() OVER
    (
        ORDER BY SUM(amount) DESC
    ) row_num

FROM master_dataset
GROUP BY customer_id;

-- #4 Top 3 spenders in every state
with new_table as(
select state, customer_id, sum(amount) as total_spending,
DENSE_RANK() OVER( partition by state order by sum(amount) desc)rn

from master_dataset group by state, customer_id)
select * from new_table where rn<=3;

-- #5 Each Customer's Largest transaction without MAX()
SELECT * FROM (SELECT *,ROW_NUMBER() OVER
(PARTITION BY customer_id ORDER BY amount DESC
) rn
FROM master_dataset
)t
WHERE rn=1;

-- #6 Calculate the difference between current and previous transaction.
select customer_id, transaction_time, amount, amount- LAG(amount) OVER
(
PARTITION BY customer_id
ORDER BY transaction_time
)
AS difference FROM master_dataset;

-- #7 Find customers whose spending increased compared to their previous transaction.
WITH t AS(SELECT customer_id, transaction_time, amount,
LAG(amount) OVER
(
PARTITION BY customer_id ORDER BY transaction_time
)
previous_amount FROM master_dataset
)

SELECT * FROM t
WHERE amount>previous_amount;

-- #8 Transaction amount for every month along with the percentage growth compared to the previous month.
WITH monthly_sales AS
(
    SELECT
        DATE_TRUNC('month', transaction_time) AS month,
        SUM(amount) AS total_sales
    FROM master_dataset
    GROUP BY DATE_TRUNC('month', transaction_time)
),

growth AS
(
    SELECT
        month,
        total_sales,
        LAG(total_sales) OVER (ORDER BY month) AS previous_month
    FROM monthly_sales
)

SELECT
    month,
    total_sales,
    previous_month,

    ROUND(
        (
            ((total_sales - previous_month) * 100.0) / previous_month
        )::numeric,
        2
    ) AS growth_percent

FROM growth;

-- #9 Divide customers into income bands.
SELECT

CASE

WHEN annual_income<500000
THEN 'Low'

WHEN annual_income<1000000
THEN 'Middle'

WHEN annual_income<2000000
THEN 'Upper'

ELSE 'Premium'

END income_group,

ROUND(AVG(amount)::numeric,2) avg_spending,

SUM(amount) total_spending

FROM master_dataset 
GROUP BY income_group

ORDER BY total_spending DESC;


-- #10 Create a customer score.
-- Score = 50% Total Spending + 30% Number of Transactions + 20% Cards Owned 

WITH customer_metrics AS
(
SELECT

customer_id,

SUM(amount) total_spending,

COUNT(transaction_id) transactions,

COUNT(DISTINCT card_id) cards

FROM master_dataset

GROUP BY customer_id
)

SELECT

customer_id,

total_spending,

transactions,

cards,

(
0.5*total_spending+
0.3*transactions+
0.2*cards
)
customer_score

FROM customer_metrics

ORDER BY customer_score DESC;



