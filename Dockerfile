FROM python:3.13-slim-bullseye

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
