FROM python:3.8.10
# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

RUN pip install "poetry==1.2.0"
RUN poetry config virtualenvs.create false

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install
COPY ner_demo ./ner_demo
CMD tail -f /dev/null