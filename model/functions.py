import os
import utils.data_base as database
from model.bot import bot
from utils.cfg import cfg
from pydub import AudioSegment


def dir_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


def save_voice(user_id, file_id):
    """ saving voice message to disk and make a note in database"""
    path = os.path.join(cfg.OUTDIR, str(user_id))
    if not dir_exists(path):
        os.makedirs(os.path.join(path, 'voice'))
    path = os.path.join(path, 'voice')

    file_info = bot.get_file(file_id)
    file_name = file_info.file_path.split('/')[-1]
    file = bot.download_file(file_info.file_path)

    path_to_file = os.path.join(path, file_name)
    with open(path_to_file, 'wb') as f:
        f.write(file)

    path_to_voice = os.path.join(str(user_id), 'voice')
    database.insert_voice_message(user_id, os.path.join(path_to_voice, file_name))
    convert_to_wav(user_id)


def convert_to_wav(uid):
    """convert all voice messages of user to wav format with 16kHZ
    :argument uid: int, user_id
    """
    if not isinstance(uid, int):
        raise TypeError('except int, but get {}'.format(uid))

    for path in database.get_paths_voice_of_user(uid):
        print(path)
