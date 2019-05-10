FROM python:3.6-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry install

COPY . .

EXPOSE 8080
ENTRYPOINT ["poetry", "run", "gunicorn", "main:app", "--bind", "0.0.0.0:8080" ]
