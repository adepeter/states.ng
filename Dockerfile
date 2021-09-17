FROM python
ARG statesng_environment=development
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
    uwsgi-plugin-python3 \
    uwsgi-plugins-all
RUN useradd -m statesng
RUN pip install --upgrade pip
USER statesng
COPY . /srv/http/statesng
WORKDIR /srv/http/statesng
ENV STATESNG_ENVIRONMENT sleekforum.settings.$statesng_environment
RUN pip install -r requirements.txt --no-warn-script-location
# CMD ["uwsgi", "--emperor", "uwsgi.ini"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
EXPOSE 8000
