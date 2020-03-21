FROM python:3.7

COPY entrypoint.py /entrypoint.py

ENTRYPOINT python /entrypoint.py