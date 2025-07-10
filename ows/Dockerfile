FROM ghcr.io/opendatacube/ows:1.9.2

USER root

RUN apt-get update && \
    apt-get install -y \
        # python3-pip \
        # git \
        postgresql-client \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

# RUN pip3 install --break-system-packages \
#     datacube[postgres] \
#     "git+https://github.com/opendatacube/datacube-ows.git@add-headers-endpoint"

RUN echo "[default]" > /tmp/datacube.conf

COPY ./ows_config /env/config/ows_config
