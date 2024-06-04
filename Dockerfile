FROM python:3.12.3-alpine3.20
RUN apk add --no-cache openjdk21 g++ gcc

WORKDIR /app

# update and install given packages
# apk is Alpine Linux package system

# --no-cache means pip will always download the package, even if it has been downloaded before.
# trade-off between speed during package installation & disk space
COPY requirements.txt requirements.txt 
RUN pip install --no-cache -r requirements.txt

# Copying from root directory of host to working directory of image
COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

# For inter-communication among containers and tells that we intend to use port 8000
EXPOSE 8000

# Setting up the environment variables
# NOTE - space after equal sign is not allowed 
# DJANGO_SETTINGS_MODULE= Code_Verdict.settings --> gives error
ENV DJANGO_SETTINGS_MODULE=Code_Verdict.settings

# python output -> stdout and stderr streams are sent straight to terminal like logs without being first buffered
# => can see output in real time + ensures that no partial output is held in buffer somewhere and never written in case python crashes.
# PYTHONUNBUFFERED has absolutely no effect on input (i.e. the stdin stream)
ENV PYTHONUNBUFFERED = 1

# Run only once when container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]