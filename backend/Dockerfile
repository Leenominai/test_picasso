FROM python:3.9-slim-buster

RUN pip3 install --upgrade pip && pip3 install poetry

WORKDIR /backend

COPY poetry.lock pyproject.toml entrypoint.sh ./

RUN poetry config virtualenvs.create false && poetry install --without test --no-interaction --no-ansi

COPY filemanager /backend

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

CMD ["gunicorn", "filemanager.wsgi:application", "--bind", "0:8000" ]
# CMD ["gunicorn", "filemanager.wsgi:application", "--bind", "0:8000", "--timeout", "60"]

LABEL author='leenominai' version='develop v1.0' broken_keyboards=1
