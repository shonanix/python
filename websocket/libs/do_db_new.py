import os
import sys
import records
import pandas as pd
from sqlalchemy.orm import sessionmaker
from libs.readconfig import *
from sqlalchemy import create_engine, text
from configparser import ConfigParser

cfg = readconfig()
DEFAULT_CONFIG = cfg


class SerializerConfig:
    instance = {}

    def __init__(self, section='database', config=DEFAULT_CONFIG):
        self.section = section
        self.attrs = config.items(section)
        for k, v in dict(self.attrs).items():
            setattr(self, k, v)

    def __getitem__(self, key):
        return getattr(self, key, False)

    def __new__(cls, *args, **kwargs):
        if cls not in cls.instance:
            cls.instance[cls] = super().__new__(cls)
        return cls.instance[cls]

    @property
    def fields(self):
        return {k: v for k, v in self.__dict__.items() if k not in ('section', 'attrs')}


head = {
    'postgresql': 'postgresql+psycopg2',
    'mysql': 'mysql+pymysql',
    'oracle': 'oracle',
    'sqlserver': 'mssql+pymssql',
}


def generate_db_url(source):
    url = f"{head[source['source_type']]}://{source['user_name']}:{source['password']}@" \
          f"{source['ip']}:{source['port']}/{source['database']}?{source['charset']}"
    return url


def get_db_url(source=None):
    if not os.environ.get('database'):
        if not source:
            source = SerializerConfig()
            if 'charset' not in source.fields:
                setattr(source, 'charset', 'utf-8')
    else:
        source = {
            'source_type': os.environ.get('db_type', 'postgresql'),
            'user_name': os.environ.get('db_user', 'postgres'),
            'password': os.environ.get('db_pass', 'pgpasswd'),
            'port': os.environ.get('db_port', '5432'),
            'ip': os.environ.get('db_addr'),
            'database': os.environ.get('db_database'),
            'charset': os.environ.get('charset', 'utf-8')
        }
    url = generate_db_url(source)
    # url = f"{url}/{source['database']}" if source['source_type'] != 'sqlserver' else url
    return url


DEFAULT_DB_URL = get_db_url()


class HandleDB:
    instance = {}

    def __init__(self, db_url=DEFAULT_DB_URL, source=None):
        if not source:
            self.db_url = db_url
        else:
            self.db_url = generate_db_url(source)
        self._db = records.Database(self.db_url)

    @property
    def db(self):
        return self._db

    # def __new__(cls,  *args, **kwargs):
    #     if cls not in cls.instance:
    #         cls.instance[cls] = super().__new__(cls)
    #     return cls.instance[cls]

    def get_sql_data(self, sql=None):
        # if 'mssql' not in self.db_url:
        #     return self._db.query(sql).export('df')
        # else:
        data = []
        engine = create_engine(self.db_url, encoding="utf-8")
        conn = engine.connect()
        try:
            if isinstance(sql, list):
                for s in sql:
                    data.append(pd.read_sql(text(s), conn))
            else:
                data.append(pd.read_sql(text(sql), conn))
        finally:
            conn.close()
            engine.dispose()
            return pd.concat(data, ignore_index=True) if data else pd.DataFrame()

    def insert(self, sql):
        engine = create_engine(self.db_url, encoding="utf-8")
        conn = engine.connect()
        try:
            conn.execute(sql)
        finally:
            conn.close()
            engine.dispose()


if __name__ == '__main__':
    sql_conn = get_db_url()
    hd = HandleDB(sql_conn)
    # rows = hd.handle_db("SELECT * FROM boiler_records")
    # # print(rows)
    rows = hd.db.query("""select * from "base_dwd"."heatboiler_m_history" limit 10""")
    for row in rows:
        print(row.pid)


