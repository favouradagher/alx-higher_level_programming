-- Import the given table dump into the hbtn_0c_0 database
-- Make sure to adjust the file path to the actual location of the dump file
SOURCE /path/to/table_dump.sql;

-- Display the average temperature by city, ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
