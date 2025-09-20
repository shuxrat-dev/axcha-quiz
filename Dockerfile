FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["sh", "-c", "python ping.py & python bot.py"]
