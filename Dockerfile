FROM python:3.9

WORKDIR /code


RUN apt-get update -y && \
    apt-get install -y python-scipy\
    python-numpy python-pandas &&\
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 5000

CMD ["python3", "main.py"]
