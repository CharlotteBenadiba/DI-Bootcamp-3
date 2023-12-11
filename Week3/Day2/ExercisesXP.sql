-- Exercise 1 : Items And Customers

-- We created these tables yesterday (to perform ExercisesXP)
-- CREATE TABLE IF NOT EXISTS items (
--    item_id int PRIMARY KEY,
--    item_name varchar (255),
--    price decimal (10, 2)
-- );

-- INSERT INTO items (item_id, item_name, price)
-- VALUES
--     (1, 'Small Desk', 100),
--     (2, 'Large Desk', 300),
--     (3, 'Fan', 80);
	
-- CREATE TABLE IF NOT EXISTS customers (
--     customer_id INT PRIMARY KEY,
--     first_name VARCHAR(255),
--     last_name VARCHAR(255)
-- );

-- INSERT INTO customers (customer_id, first_name, last_name)
-- VALUES
--     (1, 'Greg', 'Jones'),
--     (2, 'Sandra', 'Jones'),
--     (3, 'Scott', 'Scott'),
--     (4, 'Trevor', 'Green'),
--     (5, 'Melanie', 'Johnson');
	
-- Task 1. All items, ordered by price (lowest to highest).
-- SELECT * FROM items
-- ORDER BY price;

-- Task 2. Items with a price above 80 (80 included), ordered by price 
-- (highest to lowest).
-- SELECT * FROM items
-- WHERE price >= 80
-- ORDER BY price DESC;

-- Task 3. The first 3 customers in alphabetical order of the first 
-- name (A-Z) – exclude the primary key column from the results.
-- SELECT first_name, last_name FROM customers
-- ORDER BY first_name
-- LIMIT 3;

-- Task 4. All last names (no other columns!), in reverse 
-- alphabetical order (Z-A)
-- SELECT last_name FROM customers
-- ORDER BY last_name DESC;


-- Exercise 2 : Dvdrental Database

-- 
