--intro query, select all records from the actor table
SELECT *
FROM actor;

-- query for first_name and last_name from the actor table
SELECT first_name, last_name
FROM actor;


SELECT first_name, last_name
FROM actor
WHERE first_name = 'Nick';

--Query for first_name that LIKE Nick
SELECT first_name, last_name, actor_id
FROM actor
WHERE first_name = 'Nick';

SELECT first_name, last_name, actor_id
FROM actor
WHERE first_name LIKE 'Nick';

--% wild card - can take the place of any character
SELECT first_name, actor_id
FROM actor
WHERE actor.first_name = 'J%';

--Query for all first_name data that starts with the letter K and is followed by 2 characketers using the where Clause--
SELECT first_name, actor_id
FROM actor
WHERE first_name
LIKE 'K--';
SELECT first_name, actor_id
FROM actor
WHERE first_name
LIKE 'K,_m';

--Query for all first_name data that starts with a K and ends with th
--using the WHERE clause with both wildcard and underscore
SELECT first_name, last_name, actor_id
FROM actor
WHERE first_name LIKE 'K%th';

--Comparison Operators
--Greater Than > Less than <
--Greater or Equal >= Less Than or Equal <=
-- not equal <>

--Explore data from payment table with SELECT ALL query *
--Good idea to grab all data from a new table so you know what youre working with
SELECT * 
FROM payment;

--Query for data that shows customers who paid
-- an amount greater than $3
SELECT customer_id, amount
FROM payment 
WHERE amount > 3.00;

--Query for customers who paid under 7.99 for specific rentals
SELECT customer_id, rental_id, amount
FROM payment
WHERE amount <7.99;

--Query for payments that were greater than or equal to 5.99
SELECT customer_id, rental_id, amount
from PAYMENT
where AMOUNT >= 5.99;

--query for payments that were greater than or equal 2.99
SELECT customer_id, rental_id, amount
FROM payment
WHERE amount <=2.99;

--ORDER BY
--BETWEEN
--Query for all data
SELECT *
FROM payment
ORDER BY amount ASC; --defaults to ascending

--order by descending
SELECT *
FROM payment
ORDER BY amount DESC;

--Query for data that shows customers who paid an amount BETWEEN 2.00 and 7.99
--using WHERE, BETWEEN, and AND
SELECT customer_id, amount
FROM payment
WHERE amount BETWEEN 2.99 AND 5.99;

--Query for all customers who paid over 0.00
SELECT customer_id, amount
FROM payment
WHERE amount <> 0.00
ORDER BY amount;

--SQL Aggregations --> SUM(), AVG(), COUNT(), MIN(), MAX()

--query to display sum of amounts paid over 5.99
SELECT SUM(amount)
FROM payment
WHERE amount > 5.99;

--Average amount for payments over 4.99
SELECT AVG(amount)
FROM payment
WHERE amount > 5.99;

--Query to display the COUNT of amounts paid
SELECT COUNT(amount)
FROM payment
WHERE amount > 5.99;

--Query to display the DISTINCT COUNT of amounts paid ,-- unique values
SELECT COUNT(DISTINCT amount)
FROM payment
WHERE amount > 5.99;

--Query for smallest payment made over 7.99
SELECT MIN(AMOUNT) AS min_num_payments
FROM payment
WHERE amount > 7.99;

SELECT amount
FROM payment
WHERE amount > 7.99
ORDER BY amount -- defaults to ASC
LIMIT 10;

--SELECT the Largest amount greater than 7.99
SELECT MAX(amount) as max_num_payments
FROM payment
WHERE amount > 7.99;

SELECT amount
FROM payment 
WHERE amount > 7.99
ORDER BY amount DESC
LIMIT 1;

SELECT amount
FROM payment
WHERE amount = 7.99;

--Query to display diffrent COUNTS of amounts grouped together
SELECT amount, COUNT(amount)
FROM payment
GROUP BY amount
ORDER BY amount;

-- Query to display customer_ids with summed amounts for each customer_id
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
ORDER BY SUM(amount);


--grab all amounts by customer id
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id, amount;


SELECT *
FROM address;


--QUESTION 1:
SELECT COUNT(last_name)
FROM actor
WHERE last_name = 'Wahlberg';


--QUESTION 2:
SELECT COUNT(amount)
from payment
WHERE amount BETWEEN 3.99 AND 5.99;

--QUESTION 3:
SELECT film_id, COUNT(film_id)
FROM inventory
GROUP BY film_id
ORDER BY COUNT(film_id) DESC;

--QUESTION 4:
SELECT COUNT(last_name)
FROM customer
WHERE last_name = 'William';

--QUESTION 5:
SELECT staff_id, COUNT(staff_id)
from rental
GROUP BY staff_id
ORDER BY COUNT(staff_id)DESC
LIMIT 1;

--QUESTION 6:
SELECT COUNT (DISTINCT district)
FROM address;

--QUESTION 7:
SELECT film_id, COUNT(actor_id) AS actor_count
FROM film_actor
GROUP BY film_id
ORDER BY actor_count DESC
LIMIT 1;

--QUESTION 8:
SELECT COUNT(last_name)
FROM customer
WHERE last_name LIKE '%es'
GROUP BY store_id
HAVING store_id = 1;

--QUESTION 9:
SELECT COUNT(amount)
FROM payment
WHERE customer_id BETWEEN 380 AND 430
GROUP BY amount
HAVING COUNT(amount) > 250;

--QUESTION 10:
SELECT COUNT(rating), rating
FROM film
GROUP BY rating 
ORDER BY COUNT(rating) DESC
LIMIT 5;


