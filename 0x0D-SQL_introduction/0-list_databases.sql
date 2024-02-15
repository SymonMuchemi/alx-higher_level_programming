--- script to list all databases
SELECT schema_name
FROM information_schema.SCHEMATA
ORDER BY schema_name;
