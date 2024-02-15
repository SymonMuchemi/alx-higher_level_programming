--- lists all the tables in the mysql database
SELECT table_name
FROM information_schema.TABLES
WHERE table_schema = 'mysql';
