FROM python:3.8-slim


WORKDIR /app


COPY . .


RUN pip install --no-cache-dir Flask Flask-Cors pandas requests


EXPOSE 5000


ENV DATABASE_URI="sqlite:///game_data.db"


CMD ["python", "./app.py"]
