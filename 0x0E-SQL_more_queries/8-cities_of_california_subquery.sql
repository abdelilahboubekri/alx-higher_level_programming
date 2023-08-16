-- Script that lists all the cities of California registered in the database
SELECT id, name -- query to list all the cities from California
FROM cities
WHERE state_id = ( -- query to get the id of California
	      SELECT id
	      FROM states
	      WHERE name = "California");
