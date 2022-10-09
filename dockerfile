FROM python:latest

RUN pip3 install pyowm

ADD getweather.py .

CMD ["python3", "getweather.py"]
