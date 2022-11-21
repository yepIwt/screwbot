from vkwave.bots import SimpleLongPollBot
import os
import db
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = SimpleLongPollBot(tokens = BOT_TOKEN, group_id = 217315377)

VK_MESSAGE_CONSTANT = 2000000000

#@bot.message_handler(bot.text_filter("/start"))
@bot.message_handler(bot.conversation_type_filter(from_what="from_chat"), bot.text_filter("/start"))
def handle_start(msg_raw) -> str:
    msg = """
        Стартовая регистрация, которую нужно будет переделать!
    """
    print(msg_raw.object.object.message.peer_id)
    if db.find_chat_id(chat_id = msg_raw.object.object.message.peer_id):
        msg = "Братан, ты, походу, домом ошибся"
    else:
        db.add_new(msg_raw.object.object.message.from_id, msg_raw.object.object.message.peer_id)
        msg = "Запомню тебя, братан"
    return msg

@bot.message_handler(bot.conversation_type_filter(from_what="from_chat"), bot.text_filter("/start"))
def handle_time(msg_raw) -> str:
    pass

if __name__ == "__main__":
    bot.run_forever()