--  Exercise 1: DVD Rental

-- 1. Get a list of all the languages, from the language table.
-- SELECT name FROM language;

-- 2. Get a list of all films joined with their languages – select the following details : 
-- film title, description, and language name.
-- SELECT f.title, f.description, l.name AS language_name
-- FROM film AS f
-- JOIN language AS l ON f.language_id = l.language_id;

-- 3. Get all languages, even if there are no films in those languages – select the 
-- following details : film title, description, and language name.
-- SELECT f.title, f.description, l.name AS language_name
-- FROM language AS l
-- LEFT JOIN film AS f ON l.language_id = f.language_id;

-- 4. Create a new table called new_film with the following columns : 
-- id, name. Add some new films to the table.
-- CREATE TABLE new_film (
--     id INT PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (id, name) VALUES
-- (1, 'Avatar'),
-- (2, 'Matrix'),
-- (3, 'Interstellar');

-- 5. Create a new table called customer_review, which will contain film reviews that 
-- customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be 
-- automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
-- Create the customer_review table
-- Create the customer_review table
-- Create the customer_review table
-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INT,
--     language_id INT,
--     title VARCHAR(255) NOT NULL,
--     score INT CHECK (score >= 1 AND score <= 10) NOT NULL,
--     review_text TEXT,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
--     FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE CASCADE
-- );

-- CREATE OR REPLACE FUNCTION update_last_update()
-- RETURNS TRIGGER AS $$
-- BEGIN
--     NEW.last_update = CURRENT_TIMESTAMP;
--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- CREATE TRIGGER update_last_update_trigger
-- BEFORE UPDATE ON customer_review
-- FOR EACH ROW
-- EXECUTE FUNCTION update_last_update();

-- 6. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES
--     (1, 1, 'Great film', 9, 'This movie is excellent!'),
--     (2, 2, 'Amazing movie', 8, 'I enjoyed watching this film.');

-- 7. Delete a film that has a review from the new_film table, what happens to the 
-- customer_review table?
-- ALTER TABLE customer_review
-- ADD CONSTRAINT fk_film_review FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE;
-- DELETE FROM new_film WHERE id = 1;

-- Exercise 2 : DVD Rental

-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- Update the language of films in customer_review
-- UPDATE film
-- SET language_id = (SELECT language_id FROM language WHERE name = 'Mandarin');

-- 2. Which foreign keys (references) are defined for the customer table? How does this 
-- affect the way in which we INSERT into the customer table?
-- If the customer table has foreign key constraints defined on the columns store_id and 
-- address_id, it means that these columns reference other tables (store and address tables, 
-- respectively). The foreign key constraints enforce referential integrity, ensuring that 
-- values in these columns must match primary key values in the referenced tables.
-- Here's how it affects INSERT operations:
-- store_id:
-- When inserting into the customer table, you must provide a valid store_id that exists 
-- in the referenced store table.
-- If you try to insert a row with a store_id that does not exist in the store table, you 
-- will get a foreign key constraint violation error.
-- So, we must ensure that any values you insert into the store_id and address_id 
-- columns in the customer table already exist in the respective referenced tables to avoid 
-- foreign key constraint violations.

-- 3. We created a new table called customer_review. Drop this table. Is this an easy 
-- step, or does it need extra checking?
-- DROP TABLE customer_review;
-- Before executing this command, consider the following points:
-- Ensure that there are no foreign key constraints referencing the customer_review table. 
-- If there are, you may need to drop those constraints first or handle them appropriately.
-- If the table contains important data, consider backing up the data before dropping the 
-- table, especially if you might need it later.
-- Verify that there are no stored procedures, triggers, or views that depend on the c
-- ustomer_review table. Dropping the table might affect the functionality of such database 
-- objects.
-- Ensure that your database user has the necessary permissions to drop tables.

-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the 
-- store yet).
-- SELECT COUNT(*) AS outstanding_rentals
-- FROM rental
-- WHERE return_date IS NULL;

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned 
-- to the store yet)






