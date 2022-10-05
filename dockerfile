FROM python:latest

#LABEL getweather="getweather.py"

WORKDIR /usr/app/src

RUN pip3 install pyowm

COPY getweather.py ./

CMD [ "python", "./getweather.py"]