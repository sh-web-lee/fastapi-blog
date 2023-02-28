# fastapi-blog
# use
- step1 install docker and mysql
- step2 运行docker build
```commandline
docker build -t fastapi-blog .
```

- step3 docker run  
必须设置mysql配置信息，包含MYSQL_HOST，MYSQL_PORT，DB，user，password  
eg:
```commandline
docker run -d -p 8000:80 -e MYSQL_HOST=192.168.10.40 fastapi-blog
```