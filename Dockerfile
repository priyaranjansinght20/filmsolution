FROM Python:3

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirement.txt
RUN pip install -r requirement.txt
COPY . /app
