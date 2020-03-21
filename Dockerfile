FROM python:3.7

CMD pip install requests

COPY entrypoint.py /entrypoint.py

ENTRYPOINT python /entrypoint.py