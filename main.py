import datetime
import pytz
from vkwave.bots import SimpleLongPollBot
import os
import db
import times
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = SimpleLongPollBot(tokens=BOT_TOKEN, group_id=217315377)

VK_MESSAGE_CONSTANT = 2000000000
my_tz = pytz.timezone('Europe/Moscow')

def msg_creator(name: str, pair_num: str, pairs: dict):
	print("MESSAGE CREATOR")
	msg = f"{name} думает смотря на часы, что\nСледующая - {pair_num}\n"

	if pairs.get("2g"):
		msg += f"""
			
			1 группа:
			Название пары: {pairs.get("1g")["title"]}
			Преподаватель: {pairs.get("1g")["teacher"]}
			Где: {pairs.get("1g")['cab']}
			2 группа:
			Название пары: {pairs.get("2g")["title"]}
			Преподаватель: {pairs.get("2g")["teacher"]}
			Где: {pairs.get("2g")['cab']}
		"""
	else:
		msg += f"""
			Название пары: {pairs.get("1g")["title"]}
			Преподаватель: {pairs.get("1g")["teacher"]}
			Где: {pairs.get("1g")['cab']}
		"""

	return msg


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


@bot.message_handler(bot.conversation_type_filter(from_what="from_chat"), bot.text_filter("/next"))
async def handle_time(event: bot.SimpleBotEvent) -> str:
	added = db.find_chat_id(chat_id=event.object.object.message.peer_id)
	user_data = (
		await bot.api_context.users.get(user_ids=event.from_id)
	).response[0]
	name = user_data.first_name

	now = datetime.datetime.fromtimestamp(event.object.object.message.date, my_tz)

	print("Вызов в", now.time())

	pairs = times.predict_next_pair(
		now_time=now.time(),
		weekday_n=now.date().weekday(),
		numer_week=now.date().isocalendar()[1]
	)

	if added:
		if not pairs:
			msg = f"{name} смотрит и смотрит на часы, а следующей пары так и не находит!"
		else:
			msg = msg_creator(name, times.get_num_pair(now.time()), pairs)

	else:
		msg = "Для начала регистрация через /start"

	await event.answer(msg)


if __name__ == "__main__":
	bot.run_forever()
