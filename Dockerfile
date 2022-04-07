FROM python:3.9
WORKDIR /code
COPY poetry.lock pyproject.toml /
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
