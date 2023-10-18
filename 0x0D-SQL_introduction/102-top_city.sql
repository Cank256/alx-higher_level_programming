-- Select the top 3 cities with the highest temperatures during July and August
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
