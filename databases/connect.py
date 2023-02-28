from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


import os

host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
database = os.getenv('DB')
user = os.getenv('user')
password = os.getenv('password')

host = host if host else '127.0.0.1'
port = port if port else '3306'
database = database if database else 'blog'
user = user if user else 'root'
password = password if password else '12.1412.5'

engine_mysql = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'%(user, password, host, port, database)
print(engine_mysql)
engine = create_engine(engine_mysql)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()