from model.bot import bot
from telebot import apihelper
from utils import cmd, data_base
from utils.cfg import cfg
from model import functions


def extract_args(arg):
    return arg.split()[1:]


@bot.message_handler(commands=['status'])
def start_message(message):
    """get name"""
    bot.send_message(message.chat.id, bot.get_me())


@bot.message_handler(commands=['clear_db'])
def clear_database(message):
    """drop table"""
    data_base.clear_table()
    bot.send_message(message.chat.id, 'DB is empty')


@bot.message_handler(commands=['convert'])
def convert_voice_msg_user(message):
    """convert all voice message of user to wav"""
    uid = extract_args(message.text)[0]
    functions.convert_to_wav(uid)


@bot.message_handler(content_types=['voice', 'photo'])
def get_attachments(message):
    """ Receives voice message or photo. If it's a voice then saves it,
    else if it's a photo then checks whether there is a face, and if there is then saves it.
    """
    user_id = message.from_user.id

    if message.content_type == 'voice':
        file_id = message.voice.file_id
        functions.save_voice(user_id, file_id)

    elif message.content_type == 'photo':
        file_id = message.photo[-1].file_id
        functions.save_img(user_id, file_id)


if __name__ == '__main__':
    args = cmd.parse_args()
    if cfg.OUTDIR is None:
        if args.path:
            cfg.OUTDIR = args.path
        else:
            raise NotADirectoryError('path to file directory not specified')
    elif args.proxy:
        apihelper.proxy = {'http': args.proxy}

    bot.polling(none_stop=True)
