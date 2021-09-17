FROM python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get upgrade -y && apt-get update && apt-get install -y \
    nano \
    libffi-dev \
    libssl-dev \
    sqlite3 \
    libjpeg-dev \
    libopenjp2-7-dev \
    locales \
    cron \
    postgresql-client \
    gettext \
    build-essential \
    python3 \
    python3-dev \
    uwsgi-plugin-python3
RUN useradd -m statesng
RUN pip install --upgrade pip
RUN pip install pipenv
USER statesng
RUN pipenv install
## USER statesng
## COPY . /srv/http/statesng
#WORKDIR /srv/http/statesng
# pip install -r requirements.txt --no-warn-script-location
CMD ["uwsgi", "uwsgi.ini"]
EXPOSE 8000
