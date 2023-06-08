

#Instructions about how we run our application


#From docker hub, pyhon image does get installed in our docker. DOckers inside dockers. 
#FROM scratch =an explicitly empty image, especially for building images "FROM scratch" as a starting point for building containers.

FROM 528963888625.dkr.ecr.eu-central-1.amazonaws.com/cruddur-python:3.10-slim-buster


# Inside container: make a new folder inside container
WORKDIR /backend-flask

# Outside container --> Inside container: copy from outside to inside. This file has the libraries we want to install
COPY requirements.txt requirements.txt

# Inside container: install the python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside container -> Inside container
# . means everything int eh current directory
# First period . -/backend-flask (outside container)
# Second period . /backend-flask (inside container)
COPY . .


# Enviroment variables
#ENV FLASK_DEBUG=1

EXPOSE ${PORT}

# Print en developent the prints and helps us. Usefull
ENV PYTHONUNBUFFERED=1 

# CMD (command)
# To run flask.  python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]