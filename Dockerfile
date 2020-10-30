FROM python:3
RUN pip install forex_python flask

CMD MainGame.py