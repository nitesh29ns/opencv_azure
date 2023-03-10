from python:3.7

COPY . . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
#ENTRYPOINT ["python", "app.py"]

CMD gunicorn --workers=3  --bind 0.0.0.0:$PORT app:app