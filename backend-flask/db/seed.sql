-- this file was manually created

--The INSERT INTO statement is used to insert new records in a table.

INSERT INTO public.users (display_name, email, handle, cognito_user_id)

VALUES
  ('El Cid','elcidsiempregana@gmail.com', 'elcidesguapo' ,'CREADOconseedFile'),
  ('Pedro','rgzledesma@gmail.com', 'pedro_user' ,'TIENEQUEACTUALIZARSE'),
  ('Andrew Brown','andrew@exampro.co' , 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko','bayko@exampro.co' , 'bayko' ,'MOCK');


INSERT INTO public.activities (user_uuid, message, expires_at)

VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'elcidesguapo' LIMIT 1),
    'Este tuit ha sido cargado mediante el fichero seed.sql',
    current_timestamp + interval '10 day'
  )
