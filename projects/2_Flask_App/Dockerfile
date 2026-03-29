#pull image for python
FROM python:3.8-slim

#set workingdirectory
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]