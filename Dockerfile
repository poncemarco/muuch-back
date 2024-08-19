FROM python:3.10.14-alpine3.20

WORKDIR /app

# RUN apk update  \
#     && pip install --upgrade pip


COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



