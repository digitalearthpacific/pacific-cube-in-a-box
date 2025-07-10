FROM ghcr.io/opendatacube/ows:1.9.2

USER root

RUN apt-get update && \
    apt-get install -y \
        postgresql-client \
    && apt-get autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

# Need these above to do the below
# python3-pip \
# git \

# RUN pip3 install --break-system-packages \
#     datacube[postgres] \
#     "git+https://github.com/opendatacube/datacube-ows.git@add-headers-endpoint"

RUN echo "[default]" > /tmp/datacube.conf

COPY ./ows_config /env/config/ows_config
