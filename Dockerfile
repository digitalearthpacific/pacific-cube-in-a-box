FROM ghcr.io/osgeo/gdal:ubuntu-small-3.9.2

# Set non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install packages
RUN apt-get update && apt-get install -y \
    python3-full \
    python3-dev \
    python3-pip \
    git \
    curl \
    ca-certificates \
    build-essential \
    # Postgres binaries and client
    postgresql-client \
    libpq-dev \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

RUN echo "update"

RUN pip3 install --break-system-packages \
    odc-stac \
    odc-geo \
    "git+https://github.com/opendatacube/datacube-core.git@develop-1.9" \
    "git+https://github.com/opendatacube/datacube-ows.git@develop-1.9" \
    "git+https://github.com/opendatacube/odc-tools.git@develop-1.9#subdirectory=apps/dc_tools" \
    "git+https://github.com/opendatacube/eo-datasets.git@integrate-1.9"

RUN datacube --version
