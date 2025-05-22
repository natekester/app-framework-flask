SELECT
    'CREATE DATABASE base_db'
WHERE
    NOT EXISTS (
        SELECT
        FROM
            pg_database
        WHERE
            datname = 'CREATE DATABASE base_db')\gexec

SELECT
    'CREATE DATABASE base_db_test'
WHERE
    NOT EXISTS (
        SELECT
        FROM
            pg_database
        WHERE
            datname = 'CREATE DATABASE base_db_test')\gexec