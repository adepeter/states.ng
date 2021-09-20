FROM archlinux
ARG statesng_user=statesng
ARG statesng_environment=development
ENV STATESNG_USER ${statesng_user}
ENV STATESNG_PATH /srv/http/${STATESNG_USER}
ENV PIPENV_VERBOSITY=-1
RUN pacman -Syu --noconfirm base-devel \
    lynx \
    nano \
    vi \
    postgresql \
    git \
    uwsgi \
    uwsgi-plugin-python \
    uwsgitop \
    python \
    python-{pip,setuptools,wheel,django} && \
    pip install --upgrade pip setuptools wheel uwsgi && \
    pacman -Scc --noconfirm
RUN useradd --create-home --shell /bin/bash ${statesng_user} && \
    echo "statesng:statesng" | chpasswd && \
    echo "${statesng_user} ALL=(ALL) ALL" >> /etc/sudoers && \
    chown -R ${statesng_user} ${STATESNG_PATH}
USER ${statesng_user}
COPY --chown=${STATESNG_USER} . ${STATESNG_PATH}
WORKDIR ${STATESNG_PATH}
ENV STATESNG_ENVIRONMENT ${STATESNG_USER}.settings.${statesng_environment}
RUN pip install -r requirements.txt --no-warn-script-location
CMD ["uwsgi", "--emperor", "uwsgi.ini"]
EXPOSE 8000
