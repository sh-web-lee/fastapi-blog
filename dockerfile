FROM python:3.7
WORKDIR /home
COPY . /home
EXPOSE 80
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip3 config set install.trusted-host mirrors.aliyun.com
RUN pip3 install -r requirements.txt
CMD ["python","main.py"]