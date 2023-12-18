FROM opendatacube/ows:1.8.36

USER root

RUN apt-get update && \
    apt-get install -y python3-pip &&\
    apt-get autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/{apt,dpkg,cache,log}

RUN pip3 install planetary_computer && pip3 freeze

COPY ./ows_config /env/config/ows_config

USER ows
