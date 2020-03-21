FROM python:3.7

RUN pip install requests

COPY entrypoint.py /entrypoint.py

ENTRYPOINT python /entrypoint.py