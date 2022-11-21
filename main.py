from vkwave.bots import SimpleLongPollBot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = SimpleLongPollBot(tokens = BOT_TOKEN, group_id = 217315377)


@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"


if __name__ == "__main__":
    bot.run_forever()