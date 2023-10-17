-- Import the given table dump into the hbtn_0c_0 database
-- Make sure to adjust the file path to the actual location of the dump file
SOURCE /path/to/table_dump.sql;

-- Display the max temperature of each state ordered by state name
SELECT state, MAX(temperature) AS max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;
