--#1 Top 10 customers who have spent the highest total amount.
select distinct first_name, round(sum(amount)::numeric,2) as total_spending from master_dataset
group by first_name order by total_spending desc limit 10;

-- #2 Top 5 merchant categories based on total transaction amount
select merchant_id, round(sum(amount)::numeric,2) as total_amount from master_dataset
group by merchant_id order by total_amount desc limit 5;

-- #3 Average transaction amount for every card type
select card_type, round(avg(amount)::numeric,2) as average_transaction from master_dataset 
group by card_type order by average_transaction desc;

-- #4 State having highest total spending
select state, round(sum(amount)::numeric) as spending from master_dataset
group by state order by spending desc limit 1;

-- #5 Find all merchants where the average transaction amount exceeds the overall average transaction amount.
select merchant_id , round(avg(amount)::numeric,2) as avg_transaction from master_dataset 
 group by merchant_id having avg(amount) >(select avg(amount) from master_dataset) order by avg_transaction desc;