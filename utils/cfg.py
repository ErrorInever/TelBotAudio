from easydict import EasyDict as edict

__C = edict()


# Consumers can get config by:
cfg = __C


# API TOKEN
__C.TOKEN = None

# path to directory where all files will be stored
__C.OUTDIR = None
# path to directory where converted files will be stored
__C.OUT_DIR_WAV = None
# path to database
__C.DB_PATH = r'uid.db'


# Table scheme
# CREATE TABLE voices (
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
# 	uid INTEGER NOT NULL,
# 	voice_path TEXT NOT NULL
# );

# SQL queries
__C.SQL_INSERT_QUERY_VOICE = """INSERT INTO voices (uid, voice_path) VALUES (?, ?)"""
__C.SQL_SELECT_QUERY_VOICE = """SELECT voice_path FROM voices WHERE uid == (?)"""
__C.SQL_CLEAR_TABLE = """DELETE FROM voices"""
