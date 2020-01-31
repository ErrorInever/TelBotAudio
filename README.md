# Simple telegram bot

A simple bot which saves voice messages or photos of users (if there are faces in photos), in addition, can downsampling and converts voice messages to wav.

# Works on python 3.7 and lower

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
 3. after all execute **handlers.py**
    
Bot Commands:

/convert user_id - converts all voice messages of user_id for all records from database.
