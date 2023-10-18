-- List all cities with their state names
SELECT cities.id, cities.name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
