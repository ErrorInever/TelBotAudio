from model.bot import bot
from telebot import apihelper
from utils import cmd
from utils.cfg import cfg
from model import functions


@bot.message_handler(commands=['status'])
def start_message(message):
    """check auth"""
    bot.send_message(message.chat.id, bot.get_me())


@bot.message_handler(content_types=['voice', 'photo'])
def get_attachments(message):
    user_id = message.from_user.id

    if message.content_type == 'voice':
        file_id = message.voice.file_id
        functions.save_voice(user_id, file_id)

    elif message.content_type == 'photo':
        pass


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
