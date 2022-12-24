import datetime
from tables import ib11bo

timetable_pairs = {
	datetime.time(hour=9, minute=0): "Первая пара",
	datetime.time(hour=10, minute=45): "Вторая пара",
	datetime.time(hour=13, minute=20): "Третья пара",
	datetime.time(hour=15, minute=5): "Четвертая пара",
	datetime.time(hour=16, minute=50): "Пятая пара",
	datetime.time(hour=18, minute=35): "Шестая пара",
}

days_in_strings = {
	0: "Monday",
	1: "Tuesday",
	2: "Wensday",
	3: "Thursday",
	4: "Friday",
	5: "Saturday",
	6: "Sunday",
}


def get_num_pair(t: datetime.time):
	next_para = None

	for pairs in timetable_pairs.keys():
		if pairs > t:
			next_para = pairs
			break

	if t < datetime.time(hour=9, minute=0):
		next_para = datetime.time(hour=9, minute=0)

	if not next_para:
		return "Пары кончились на сегодня"

	next_para = timetable_pairs.get(next_para)

	return next_para


def predict_next_pair(now_time: datetime.time, weekday_n: int, numer_week: int) -> str:
	print("started predicted")

	weekday = days_in_strings[weekday_n]
	next_para = get_num_pair(now_time)
	print(next_para)

	den_or_num = "denominator" if numer_week % 2 == 0 else "numerator"

	if not ib11bo.timetable.get(den_or_num).get(weekday):
		return False
	else:
		res = ib11bo.timetable.get(den_or_num).get(weekday).get(next_para)
	print("RES TIME", res)
	return res
