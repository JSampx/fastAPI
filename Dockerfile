FROM python:3.12-alpine3.20
EXPOSE 5000
WORKDIR /fastapi
COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]