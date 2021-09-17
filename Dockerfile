FROM archlinux
ARG statesng_user=statesng
ENV STATESNG_USER=$statesng
ENV STATESNG_PATH /srv/http/$STATESNG_USER
ENV PIPENV_VERBOSITY=-1
RUN pacman -Syu --noconfirm base-devel \
    lynx \
    nano \
    postgresql \
    git \
    uwsgi \
    uwsgi-plugin-python \
    uwsgitop \
    python \
    python-{pip,setuptools,wheel} && \
    pip install --upgrade pip setuptools wheel uwsgi && \
    pacman -Scc --noconfirm
RUN useradd --create-home -G sudo $statesng_user && \
    echo "statesng:statesng" | chpasswd && \
USER $statesng_user
COPY --chown=$STATESNG_USER . $STATESNG_PATH
WORKDIR $STATESNG_PATH
ENV STATESNG_ENVIRONMENT statesng.settings.$statesng_environment
RUN pip install -r requirements.txt --no-warn-script-location
CMD ["uwsgi", "uwsgi.ini"]
EXPOSE 8000
