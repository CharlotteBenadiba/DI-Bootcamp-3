-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('Angelina', 'Jolie', '1975-06-04', 1);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('Jennifer', 'Aniston', '1969-02-11', 0);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
--     ('Brad', 'Pitt', '1963-12-18', 1),
--     ('Julia', 'Roberts', '1967-10-28', 1),
--     ('Leonardo', 'DiCaprio', '1974-11-11', 1);
	
-- Retrieve the first 4 actors
-- SELECT * FROM actors
-- LIMIT 4;

-- Retrieve the first 4 actors ordered by last_name in descending order
-- SELECT * FROM actors
-- ORDER BY last_name DESC
-- LIMIT 4;

-- Retrieve actors with the letter 'e' in their first_name
-- SELECT * FROM actors
-- WHERE LOWER(first_name) LIKE '%e%';

-- Retrieve actors with at least 5 oscars
-- SELECT * FROM actors
-- WHERE number_oscars >= 5;

-- Update the first name of Matt Damon to "Maty"
-- UPDATE actors
-- SET first_name = 'Maty'
-- WHERE first_name = 'Matt';

-- -- Update the number of oscars of George Clooney to 4 and return the updated record
-- UPDATE actors
-- SET number_oscars = 4
-- WHERE last_name = 'Clooney'
-- RETURNING *;

-- -- Rename the 'age' column to 'birthdate'
-- ALTER TABLE actors
-- RENAME COLUMN age TO birthdate;

-- -- Delete one actor and return it
-- DELETE FROM actors
-- WHERE actor_id = (SELECT actor_id FROM actors LIMIT 1)
-- RETURNING *;

-- Count how many actors are in the table
-- SELECT COUNT(*) FROM actors;

-- Try to add a new actor with some blank fields
-- INSERT INTO actors (first_name, last_name)
-- VALUES ('Johnny', 'Depp');

-- The outcome will depend on the table's constraints. 
-- In the provided table definition, both first_name and last_name 
-- columns are marked as NOT NULL, which means they cannot have NULL 
-- values. Attempting to insert a new actor with blank fields will 
-- result in an error. The error indicates that the age column cannot 
-- have a null value, violating the NOT NULL constraint. To add a new 
-- actor, you should provide values for all the columns that don't 
-- allow nulls, or modify the table structure to allow nulls in specific
-- columns if it's appropriate for your use case.

-- Thus, to add an actor to the table, you need to specify data 
-- for all columns:
INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
VALUES ('Johnny', 'Depp', '1963-06-09', 0);





