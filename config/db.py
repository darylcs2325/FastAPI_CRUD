from sqlalchemy import create_engine, MetaData
from configparser import ConfigParser

config = ConfigParser()
config.read('config/cfg.ini')
postgres = config['POSTGRES']['CONNSTR']
print(postgres)
meta = MetaData()

engine = create_engine(postgres)
conn = engine.connect()