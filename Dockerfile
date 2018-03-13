FROM python:3-alpint
ADD *.py /
RUN pip3 install python-telegram-bot pyowm
CMD [ "python3", "/weather.py" ]
