import datetime

timetable = {
	datetime.time(hour=9, minute=0): "Первая пара",
	datetime.time(hour=10, minute=45): "Вторая пара",
	datetime.time(hour=13, minute=20): "Третья пара",
	datetime.time(hour=15, minute=5): "Четвертая пара",
	datetime.time(hour=16, minute=50): "Пятая пара",
	datetime.time(hour=18, minute=35): "Шестая пара",
}


now = datetime.datetime.now().time()
now = datetime.time(hour=12, minute=20)

def predict_next_pair(now_time: datetime.time) -> str:
	next_para = None

	if now_time < datetime.time(hour=12, minute = 20):
		return "Перерыв 1 час"

	for pairs in timetable.keys():
		if pairs > now:
			next_para = pairs
			break

	return timetable.get(next_para)

print(predict_next_pair(now))
