#Pull MYQK image
FROM mysql:8.0

#Set environment variable
ENV MYSQL_ROOT_PASSWORD=demopassword
ENV MYSQL_DATABASE=demodb

#copy initialization script to rhe Docker Image
COPY init.sql /docker-entrypoint-initdb.d/

#expose sql port
EXPOSE 3307