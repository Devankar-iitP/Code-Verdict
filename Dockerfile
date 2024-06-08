FROM python:3.12.3-alpine3.20
RUN apk add --no-cache openjdk21 g++ gcc

WORKDIR /app

# python output -> stdout and stderr streams are sent straight to terminal like logs without being first buffered
# => can see output in real time + ensures that no partial output is held in buffer somewhere and never written in case python crashes.
# PYTHONUNBUFFERED has absolutely no effect on input (i.e. the stdin stream)
ENV PYTHONUNBUFFERED=1

# --no-cache means pip will always download the package, even if it has been downloaded before.
# trade-off between speed during package installation & disk space
COPY requirements.txt requirements.txt 
RUN pip install --no-cache -r requirements.txt

# Copying from root directory of host to working directory of image
COPY . .

# For inter-communication among containers and tells that we intend to use port 8000
EXPOSE 8000