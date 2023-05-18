-- this file was manually created

--The INSERT INTO statement is used to insert new records in a table.

INSERT INTO public.users (display_name, email, handle, cognito_user_id)

VALUES
  ('El Cid','elcidsiempregana@gmail.com', 'elcidesguapo' ,'CREADOconseedFile'),
  ('Pedro','rgzledesma@gmail.com', 'pedro_user' ,'TIENEQUEACTUALIZARSE'),
  ('Andrew Brown','andrew@exampro.co' , 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko','bayko@exampro.co' , 'bayko' ,'MOCK'),
  ('Londo Mollari', 'lmollari@centari.com','londo','MOCK');


INSERT INTO public.activities (user_uuid, message, expires_at)

VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'elcidesguapo' LIMIT 1),
    'Este tuit ha sido cargado mediante el fichero seed.sql. Puede estar de forma local o en la nube',
    current_timestamp + interval '10 day'
  );

INSERT INTO public.activities (user_uuid, message, expires_at)

VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'pedro_user' LIMIT 1),
    'Este tuit ha sido cargado mediante el fichero seed.sql y es de pedro_user',
    current_timestamp + interval '30 day'
  );