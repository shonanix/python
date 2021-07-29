import requests
import psycopg2
import traceback
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from libs.readconfig import *
from libs.logger import Logger

config = readconfig()
print_logging = Logger(__file__).get_log()


class DBProcess(object):

    def __init__(self):

        self.config = readconfig()
        self.host = self.config.get('postgres', 'host')
        self.port = self.config.get('postgres', 'port')
        self.user = self.config.get('postgres', 'user')
        self.password = self.config.get('postgres', 'password')
        self.dbname = self.config.get('postgres', 'dbname')
        self.saveurl = "postgresql://%s:%s@%s:%s/%s" % (self.user, self.password, self.host, self.port, self.dbname)
        self.schema = self.config.get('database', 'mode')

    def Data_to_sql(self,sql):
        """ 将数据写入数据库
        :return:
        """
        engine = create_engine(self.saveurl)

        # 创建DBSession类型:
        conn = engine.raw_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def DataIntoTimescale(self, data, table):
        """ 将数据写入数据库
        :return:
        """
        engine = create_engine(self.saveurl)

        try:
            data.to_sql(table, engine, schema=self.schema, if_exists='append', index=False, chunksize=200)
        finally:
            engine.dispose()

    def handle_sql(self, sql):
        """ 数据库查询
        :return:
        """
        rows = []
        try:
            conn = psycopg2.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, dbname=self.dbname)

            if 'select' not in sql and 'SELECT' not in sql:
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                conn.close()
                cur.close()
            else:
                rows = pd.read_sql(sql, conn)
                conn.close()

        except ConnectionError:
            traceback.print_exc()
        finally:
            return rows

