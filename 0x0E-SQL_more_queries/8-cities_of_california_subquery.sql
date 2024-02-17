-- cities of califonia subquery
SELECT cities.id, cities.state_id, states.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
