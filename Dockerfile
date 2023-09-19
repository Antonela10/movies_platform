FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install django==4.1
COPY . /app/

EXPOSE 8000

CMD ["sh", "run"]