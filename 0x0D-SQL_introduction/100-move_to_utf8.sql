-- that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- the following will be converted to UTF8:
    -- Database
    -- first_table
    -- name in first_table
ALTER DATABASE alx_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
