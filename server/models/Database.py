import json

import psycopg2 as pg2


# def get_db_config(path):
#     try:
#         config = json.load(open(path, 'r'))
#     except (Exception, IOError) as error:
#         if type(error) == IOError:
#             print("DB config IO errors.")
#         print(error)
#     finally:
#         return config
#
#
# def connect_db():
#     config = get_db_config('../config/db_config')
#     try:
#         connection = pg2.connect(user=config['user'], password=config['password'],
#                                        host=config['host'], port=config['port'],
#                                        database=config['database'])
#         cursor = connection.cursor()
#     except (Exception, pg2.Error) as error:
#         if type(error) == pg2.Error:
#             print("Psycopg2 connection errors.")
#         print(error)
#     finally:
#         return connection, cursor


class Database:
    def __init__(self, config_file):
        self.__conn = None
        self.__cur = None
        try:
            self.__config = json.load(open(config_file, 'r'))
            self.connect_db()
        except (Exception, IOError, pg2.Error) as error:
            if type(error) == IOError:
                print("DB config IO errors.")
            print(error)

    def connect_db(self):
        try:
            if (self.__conn is None) or (not self.is_connected()):
                self.__conn = pg2.connect(user=self.__config['user'], password=self.__config['password'],
                                          host=self.__config['host'], port=self.__config['port'],
                                          database=self.__config['database'])
        except (Exception, pg2.Error) as error:
            if type(error) == pg2.Error:
                print("Psycopg2 connection errors.")
            print(error)

    def get_conn(self):
        return self.__conn

    def get_cursor(self):
        return self.__cur

    def is_connected(self):
        return self.__conn.closed == 0

    # database connection should disconnect if database is ideal of xx sec
    def disconnect_db(self):
        if self.is_connected():
            self.__conn.close()
        return self.__conn.status

    def update_table(self, query):
        try:
            self.__cur = self.__conn.cursor()
            self.__cur.execute(query)
            self.__conn.commit()
        finally:
            self.__cur.close()

    def find_one(self, query):
        row = ()
        try:
            self.__cur = self.__conn.cursor()
            self.__cur.execute(query)
            row = self.__cur.fetchone()
        finally:
            self.__cur.close()
            return row

    def find_all(self, query):
        rows = []
        try:
            self.__cur = self.__conn.cursor()
            self.__cur.execute(query)
            rows = self.__cur.fetchall()
        finally:
            self.__cur.close()
            return rows
