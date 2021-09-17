FROM archlinux
ARG statesng_user=statesng
ENV STATESNG_USER=$statesng
ENV STATESNG_PATH /srv/http/$STATESNG_USER
ENV PIPENV_VERBOSITY=-1
RUN pacman -Syu --noconfirm base-devel lynx nano git \
uwsgi uwsgi-plugin-python uwsgitop \
python python-{pip,setuptools,wheel} && \
pip install --upgrade pip setuptools wheel uwsgi && \
pacman -Scc --noconfirm
RUN useradd --create-home $statesng_user && \
    echo "statesng:statesng" | chpasswd && \
    adduser statesng sudo
USER $statesng_user
COPY --chown=$STATESNG_USER . $STATESNG_PATH
WORKDIR $STATESNG_PATH
ENV STATESNG_ENVIRONMENT statesng.settings.$statesng_environment
RUN pip install -r requirements.txt --no-warn-script-location
CMD ["uwsgi", "uwsgi.ini"]
EXPOSE 8000





















#FROM python
#ARG statesng_environment=development
#ENV PYTHONUNBUFFERED 1
#ENV PYTHONDONTWRITEBYTECODE 1
#RUN apt-get upgrade -y && apt-get update && apt-get install -y \
#    nano \
#    sudo \
#    libffi-dev \
#    libssl-dev \
#    sqlite3 \
#    libjpeg-dev \
#    libopenjp2-7-dev \
#    locales \
#    cron \
#    postgresql-client \
#    gettext \
#    build-essential \
#    python3 \
#    python3-dev \
#    uwsgi-plugin-python3 \
#    uwsgi-plugins-all
#RUN useradd -m statesng && \
#    echo "statesng:statesng" | chpasswd && \
#    adduser statesng sudo && \
#    pip install --upgrade pip
#USER statesng
#COPY --chown=statesng . /srv/http/statesng
#WORKDIR /srv/http/statesng
#ENV STATESNG_ENVIRONMENT statesng.settings.$statesng_environment
#RUN pip install -r requirements.txt --no-warn-script-location
#CMD ["uwsgi", "--emperor", "uwsgi.ini"]
#EXPOSE 8000
