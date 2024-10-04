FROM opendatacube/ows:1.9.0rc1

USER root

RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        git \
        postgresql-client \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

COPY ./ows_config /env/config/ows_config

USER ows
