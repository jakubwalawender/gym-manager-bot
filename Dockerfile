FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /gym_manager_bot
COPY requirements.txt /gym_manager_bot/
RUN pip install -r requirements.txt
COPY . /gym_manager_bot/