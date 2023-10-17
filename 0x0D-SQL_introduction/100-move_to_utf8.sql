-- You need to convert all of the following to UTF8:
--   - Database hbtn_0c_0
--   - Table first_table
--   - Field name in first_table

-- Convert the hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to UTF8
ALTER TABLE first_table MODIFY name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
