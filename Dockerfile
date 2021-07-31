FROM gorialis/discord.py:alpine-full

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]