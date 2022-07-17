FROM python:3.10.5

ENV POETRY_VERSION=1.0.0

RUN pip install "poetry==$POETRY_VERSION"

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip install --upgrade setuptools==59.6.0 \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY . /usr/src/app/

RUN cp .env.example .env

EXPOSE 8000

CMD ["uvicorn", "otus_homework_1.main:app", "--port=8000", "--host=0.0.0.0"]