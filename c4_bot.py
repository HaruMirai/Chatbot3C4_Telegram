from telegram.ext import Updater

def start(bot,update):
    update.message.reply_text("Saya bot, halo")

def main():
    updater = Updater(token='2113526663:AAGrJBGu5zB5HX2qrpbPN5ti0ycsCueaJ3I')
    disparcher = updater.dispatcher
    print("Bot Started")

if __name__=='__main__':
    main()