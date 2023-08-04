FROM python:3.8

COPY apis/src /src
WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "main.py"]