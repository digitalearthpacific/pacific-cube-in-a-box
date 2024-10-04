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

RUN pip3 install --upgrade \
        git+https://github.com/opendatacube/datacube-ows.git@develop-1.9 \
        git+https://github.com/opendatacube/datacube-core.git@develop-1.9 \
        git+https://github.com/opendatacube/odc-tools.git@develop-1.9&subdirectory=apps/dc_tools \
    && pip3 freeze

COPY ./ows_config /env/config/ows_config

USER ows
