# Pull base image for python
FROM python:3.8-slim

#container for directory in the image
WORKDIR /firstimageapp  

COPY . /firstimageapp

#run application for the container
CMD [ "python", "app.py" ]