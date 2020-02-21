ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

LABEL maintainer="Alain Sanchez<brazzisoft.com@gmail.com>" \
      company="BRAZZISOFT"  \
      project="My App Stack"

ENV PYTHONUNBUFFERED 1
ENV PYTHONOPTIMIZE 1
ENV APP_USER appuser
ENV APP_USER_UID 1000
ENV APP_GROUP appgroup
ENV APP_GROUP_GID 1000
ENV APP_HOME /app
ENV SRC_HOME $APP_HOME/src
ENV VENV_HOME $APP_HOME/venv
ENV STATIC_HOME $SRC_HOME/static
ENV MEDIA_HOME $SRC_HOME/media

ARG LOG_LEVEL=ERROR
ENV LOG_LEVEL ${LOG_LEVEL}

#
# System Configuration
# .: 1. Install apt-utils package & Required Locales
RUN apt-get -qq update && \
    apt-get -qqy install  \
    apt-utils \
    locales  \
    python-virtualenv \
    build-essential \
    gettext \
    xvfb && \
    rm -rf /var/lib/apt/lists/*
                          
# .: 2. Configure Locales dynamically
COPY ./.container/.shared/locales /locales
RUN cat /locales >> /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=en_US.UTF-8 && \
    echo "LANGUAGE=en_US.UTF-8" >> /etc/default/locale && \
    echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale

# .: 3. Set environment variables for locales
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# .: 4. Configure timezone dynamically
ARG TZ=UTC
ENV TZ ${TZ}

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    mkdir /tz && cp /etc/timezone /tz/ && cp /etc/localtime /tz/

# .: 5. Create file system Add application user and group
RUN groupadd -r -g $APP_GROUP_GID $APP_GROUP && useradd -r -u $APP_USER_UID -d $APP_HOME -g $APP_GROUP $APP_USER
RUN mkdir -p $STATIC_HOME && mkdir -p $MEDIA_HOME && mkdir -p $VENV_HOME
RUN chown -R $APP_USER:$APP_GROUP $SRC_HOME $VENV_HOME


#
# Application Configuration
# .: 1. Set the workdir to the APP_HOME
WORKDIR $APP_HOME
# .: 2. Define virtualenv environment
RUN virtualenv -p python $VENV_HOME
# .: 3. Copy requirements and install them
COPY ./requirements.txt $SRC_HOME
SHELL ["/bin/bash", "-c"]
RUN source $VENV_HOME/bin/activate && pip install -r $SRC_HOME/requirements.txt
# .: 4. Copy application
COPY . $SRC_HOME
# .: 5. Define environment variables
ENV DJANGO_SETTINGS_MODULE my_app.settings
# .: 6. Making sure all the files/folders are owned by APP_USER
RUN chown -R $APP_USER:$APP_GROUP $APP_HOME /tz
# .: 7. Setting up the docker entrypoint file
COPY ./.container/celery_worker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh && chown $APP_USER:$APP_GROUP /docker-entrypoint.sh
# .: 8. Switch context to APP_USER
USER $APP_USER

#
# Container Metadata definition
VOLUME ["$STATIC_HOME", "$MEDIA_HOME", "/tz"]

# .: Invoking Default entrypoint
CMD ["/docker-entrypoint.sh"]