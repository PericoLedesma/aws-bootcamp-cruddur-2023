-- to display the tables

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';


SELECT * FROM users;
SELECT * FROM activities;




-- Trying to loop over all the tables
/*
DO $$
DECLARE
  var1 RECORD;

BEGIN 
    FOR var1 IN (SELECT table_name FROM information_schema.tables WHERE table_schema = 'public') 
    LOOP 
        EXECUTE 'SELECT * FROM ' || var1.table_name; 
    END LOOP; 
END$$;
*/
