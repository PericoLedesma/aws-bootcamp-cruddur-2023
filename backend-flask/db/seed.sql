-- this file was manually created

--The INSERT INTO statement is used to insert new records in a table.

INSERT INTO public.users (display_name, handle, email, cognito_user_id)

VALUES
  ('El Cid', 'elcidesguapo','elcidsiempregana@gmail.com' ,'MOCK123'),
  ('Andrew Bayko', 'bayko', 'bayko@polla.es','MOCK456');


INSERT INTO public.activities (user_uuid, message, expires_at)

VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'elcidesguapo' LIMIT 1),
    'Este tuit ha sido cargado mediante el fichero seed.sql',
    current_timestamp + interval '10 day'
  )
