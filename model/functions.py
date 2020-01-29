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


def downsample(audio, khz=16000):
    """change sample rate
    :return instance of AudioSegment
    """
    if not isinstance(audio, AudioSegment):
        raise TypeError('except {}, but get {}'.format(AudioSegment.__name__, type(audio)))
    return audio.set_frame_rate(khz)


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

    # FIXME: remove from this function
    path_to_voice = os.path.join(str(user_id), 'voice')
    database.insert_voice_message(user_id, os.path.join(path_to_voice, file_name))


def convert_to_wav(uid):
    """convert all voice messages of user.
    ogg/oga to wav format and downsample to 16kHz
    :argument uid: int, user_id
    """
    for path in database.get_paths_voice_of_user(uid):
        file_name = os.path.splitext(os.path.basename(path))[0]

        voice_msg = AudioSegment.from_ogg(os.path.join(cfg.OUTDIR, path))
        voice_msg = downsample(voice_msg)
        voice_msg.export(file_name + ".wav", format="wav")
