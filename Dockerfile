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


ENV FLASK_APP=app
ENV POSTGRESQL_URI="postgresql://eshop:123@465@database/eshop"
ENV SECRET_KEY ="2F40&%3p^#h7{98o]2<AAXC@;1[&9vt;4mhktMQpX;{Zby2F40&%3p^#h#h77{98or5#`BAXC@;1[&!Ywj+D7r<AAXC@54mh#`BG|69vt;4mhktMQpX;{Zby"
USER app

ENTRYPOINT ["flask", "--app", "app", "run", "-h", "0.0.0.0", "-p", "8000", "--debug"]
#ENTRYPOINT ["gunicorn","-w","4","-b","0.0.0.0:8000" ,"app:app"]
