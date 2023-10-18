-- Select all cities with their corresponding states
SELECT c.id, c.name, (SELECT s.name FROM states s WHERE s.id = c.state_id) AS state_name
FROM cities c
ORDER BY c.id ASC;
