FROM python:3.10-alpine3.18
LABEL authors="Ehsan"

WORKDIR /src

COPY requirements.txt requirements.txt

RUN ["pip" ,"install" ,"-r","requirements.txt"]

EXPOSE 8000

COPY . .

RUN addgroup app &&  \
    adduser -S -G app app && \
    chown -R app:app /src

USER app
#ENV PATH="./Scripts:/py/bin/$PATH"

ENTRYPOINT ["flask", "run", "--debug", "-h", "0.0.0.0", "-p", "8000"]
#ENTRYPOINT ["gunicorn","-w","4","-b","0.0.0.0:8000" ,"app:app"]
