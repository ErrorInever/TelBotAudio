import os
import io
import utils.data_base as database
from model.bot import bot
from model import model
from utils.cfg import cfg
from pydub import AudioSegment
from PIL import Image


def dir_exists(path_folder, folder_name):
    """If there is no folder then creates a folder, and creates a specified folder in this folder
    else if the folder exist then checks whether there is the specified folder and if not then creates it
    :param path_folder: path to folder which we want to create
    :param folder_name: the name of folder which will be create in folder
    :return full path to the specified folder
    """
    if not os.path.exists(path_folder):
        os.makedirs(os.path.join(path_folder, folder_name))
    else:
        if not os.path.exists(os.path.join(path_folder, folder_name)):
            os.mkdir(os.path.join(path_folder, folder_name))
    return os.path.join(path_folder, folder_name)


def download_file(file_id):
    """Download file"""
    file_info = bot.get_file(file_id)
    file_name = file_info.file_path.split('/')[-1]
    file = bot.download_file(file_info.file_path)
    return file, file_name


def downsample(audio, khz=16000):
    """change sample rate to specified kHz
    :return instance of AudioSegment
    """
    if not isinstance(audio, AudioSegment):
        raise TypeError('except {}, but get {}'.format(AudioSegment.__name__, type(audio)))
    return audio.set_frame_rate(khz)


def save_voice(user_id, file_id):
    """ save voice message to disk and create a note in database"""
    path = dir_exists(os.path.join(cfg.OUTDIR, str(user_id)), 'voice')
    file, file_name = download_file(file_id)
    path_to_file = os.path.join(path, file_name)

    with open(path_to_file, 'wb') as f:
        f.write(file)

    path_to_voice = os.path.join(str(user_id), 'voice')
    database.insert_voice_message(user_id, os.path.join(path_to_voice, file_name))


def convert_to_wav(uid):
    """convert all voice messages of user.
    ogg/oga to wav format and downsample to 16kHz
    :return path
    """
    save_path = os.path.join(cfg.OUT_DIR_WAV, uid)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for path in database.get_paths_voice_of_user(uid):
        file_name = os.path.splitext(os.path.basename(path))[0] + ".wav"

        try:
            voice_msg = AudioSegment.from_ogg(os.path.join(cfg.OUTDIR, path))
        except FileNotFoundError:
            continue
        else:
            voice_msg = downsample(voice_msg)
            voice_msg.export(os.path.join(save_path, file_name), format="wav")

    return save_path


def detect_face(img):
    """
    Detects faces on an image
    :param img: instance of PIL.Image
    :return: True - if there are any face on image
             False - if there are none
    """
    detect = model.model(img)
    if detect is not None:
        return True
    return False


def save_img(user_id, file_id):
    """
    Saves an image to disk if in the image was detected a face
    """
    file, file_name = download_file(file_id)
    img_stream = io.BytesIO(file)
    img = Image.open(img_stream)

    detect = detect_face(img)
    if detect:
        path = dir_exists(os.path.join(cfg.OUTDIR, str(user_id)), 'images')
        img.save(os.path.join(path, file_name))
