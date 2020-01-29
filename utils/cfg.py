from easydict import EasyDict as edict

__C = edict()
# Consumers can get config by:
cfg = __C

# API TOKEN
__C.TOKEN = None
# OS
__C.OUTDIR = None
__C.OUT_DIR_WAV = None

# DATABASE
__C.DB_PATH = r'uid.db'

# Table scheme
# CREATE TABLE voices (
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
# 	uid INTEGER NOT NULL,
# 	voice_path TEXT NOT NULL
# );

__C.SQL_INSERT_QUERY_VOICE = """INSERT INTO voices (uid, voice_path) VALUES (?, ?)"""
__C.SQL_SELECT_QUERY_VOICE = """SELECT voice_path FROM voices WHERE uid == (?)"""
__C.SQL_CLEAR_TABLE = """DELETE FROM voices"""