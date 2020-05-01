# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' myuser

# create root directory for our project in the container
RUN mkdir /TRS

# Set the working directory to /trs
WORKDIR /TRS

# Copy the current directory contents into the container at /music_service
COPY . /TRS/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

#RUN /TRS/runserver.sh
#CMD ["/TRS/runserver.sh"]

RUN python /TRS/manage.py makemigrations booking user

RUN python /TRS/manage.py migrate

CMD [ "python", "/TRS/manage.py", "runserver", "0.0.0.0:8000" ]
