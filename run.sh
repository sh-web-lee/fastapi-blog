docker build -t fastapi-blog .
docker run -d -p 8000:80 -e MYSQL_HOST=192.168.10.40 fastapi-blog