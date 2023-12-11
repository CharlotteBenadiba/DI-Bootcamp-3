-- Daily Challenge : SQL Puzzle
-- Instructions
-- In this puzzle you have to go through all the SQL queries and provide 
-- us the output of the requests before executing them (ie. make an assumption).
-- Then, execute them to make sure you were correct.

-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)

-- SELECT * FROM SecondTab

-- Q1. This query counts the rows in FirstTab where the id is not in the set of 
-- id from SecondTab where id is NULL. So, it should count the rows where id 
-- is not NULL in FirstTab that are not present in SecondTab.

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- Q2. This query counts the rows in FirstTab where the id is not in the set of 
-- id from SecondTab where id is 5. It should count the rows where id is not 5 
-- in FirstTab.

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Q3. This query counts the rows in FirstTab where the id is not in the set of 
-- id from SecondTab. It should count the rows where id is not NULL in FirstTab 
-- that are not present in SecondTab.

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- Q4. This query counts the rows in FirstTab where the id is not in the set of 
-- id from SecondTab where id is not NULL. It should count all rows in FirstTab 
-- because all the values in SecondTab are NULL.

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )