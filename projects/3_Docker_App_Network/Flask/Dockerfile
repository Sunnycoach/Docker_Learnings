FROM python:3.9-slim

WORKDIR /appmysqlflask

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 5000

CMD [ "python","app.py" ]