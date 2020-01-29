import sqlite3
from utils.cfg import cfg


class ConnectSQL:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connect = sqlite3.connect(self.path)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()
        if exc_val:
            raise


def sql_query_execute(query, *args, select=False):
    """
    Connect to database and execute query
    :param query: string sql query
    :param args: list of arguments for query

    if select=True: return all rows of a query result
    """
    with ConnectSQL(cfg.DB_PATH) as connect:
        cursor = connect.cursor()
        cursor.execute(query, *args)

        if select:
            sample = cursor.fetchall()
            connect.commit()
            cursor.close()
            return sample

        connect.commit()
        cursor.close()


def insert_voice_message(user_id, path_voice_msg):
    """insert in table :voices: uid - path to voice message file"""
    sql_query_execute(cfg.SQL_INSERT_QUERY_VOICE, (user_id, path_voice_msg))


def get_paths_voice_of_user(user_id):
    """return generator which selects all voice messages of user_id and return path to voice message file"""
    rows = sql_query_execute(cfg.SQL_SELECT_QUERY_VOICE, (user_id,), select=True)
    rows = [x[0] for x in rows]
    yield from rows


def clear_table():
    sql_query_execute(cfg.SQL_CLEAR_TABLE)
