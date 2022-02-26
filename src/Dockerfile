FROM archlinux:base-devel
ARG statesng_user=statesng
ARG deployment_environment=development
ENV STATESNG_USER ${statesng_user}
ENV STATESNG_PATH /srv/http/${STATESNG_USER}
ENV PIPENV_VERBOSITY=-1
ENV PYTHONDONTWRITEBYTECODE=1
RUN pacman -Syu --noconfirm \
    lynx \
    nano \
    vi \
    postgresql \
    git \
    redis \
    uwsgi \
    uwsgi-plugin-python \
    uwsgitop \
    python \
    python-{pip,setuptools,wheel,django,pipenv} && \
    pip install --upgrade pip pipenv setuptools wheel uwsgi && \
    pacman -Scc --noconfirm
RUN useradd --create-home --shell /bin/bash ${statesng_user} && \
    echo "statesng:statesng" | chpasswd && \
    echo "${statesng_user} ALL=(ALL) ALL" >> /etc/sudoers
# USER ${statesng_user}
# COPY --chown=${STATESNG_USER} . ${STATESNG_PATH}
COPY . ${STATESNG_PATH}
WORKDIR ${STATESNG_PATH}
ENV DEPLOYMENT_ENVIRONMENT ${deployment_environment}
RUN pip install -r requirements.txt --no-warn-script-location
CMD ["uwsgi", "--emperor", "uwsgi.ini", "--env", "DEPLOYMENT_ENVIRONMENT=${DEPLOYMENT_ENVIRONMENT}", "--uid", "${statesng_user}", "--master"]
EXPOSE 8000
