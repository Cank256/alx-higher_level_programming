-- Calculate the average temperature in Fahrenheit by city and order by temperature (descending)
SELECT city, AVG(temperature) as avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
