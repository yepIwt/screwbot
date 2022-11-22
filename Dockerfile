FROM python:3.9.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV BOT_TOKEN="vk1.a.raDtJdWDY1eJWXnsDFtMY0-rfSePoRysRvxU28acDEoYnoyeeGAb6FuRmqSnaoEmymEe6O0nXeuDYUSOXCeihXj3qLyAQ7SJLZgtPWqcDIkejXsWfFQke-wVnEv_hUlMgo-1nfgLpCZabdKxtSFzr9XE0hFNhIMdBKIba0cnoz4d0ArMUT-ITpvuRAEktjAQ6BHGYovqgBa6R_VvDwkcag"

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","main.py"]