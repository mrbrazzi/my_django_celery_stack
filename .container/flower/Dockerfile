FROM mher/flower

USER root

# Default port
ARG FLOWER_PORT=5555
ENV FLOWER_PORT ${FLOWER_PORT}

ARG TZ=UTC
ENV TZ ${TZ}

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Run as a non-root user by default, run as user with least privileges.
USER nobody

ENTRYPOINT ["flower"]

EXPOSE $FLOWER_PORT