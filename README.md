# Simple telegram bot

### Start
1. > pip install -r requirements.txt 
2. edit **utils/cfg.py** i.e. add paths and an api token

    ```
    # API TOKEN
    __C.TOKEN = None
    # path to directory where all files will be stored
    __C.OUTDIR = None
    # path to directory where converted files will be stored
    __C.OUT_DIR_WAV = None
    # path to database
    __C.DB_PATH = r'uid.db'
    ```
    
Commands:
1. /convert uid - converts all voice messages which are stored on disk.
