.PHONY: up products index-sentinel-1

# BBOX over Samoa and Tonga
BBOX := -180.0,-20.0,-170.0,-10.0

# Bigger BBOX over most of the Pacific
BIGBBOX := 135.0,-30.0,180.0,15.0
BIGBBOX2 := -180,-30.0,-120.0,15.0

build:
	docker build --platform linux/amd64 -t ows:local ows

up:
	docker compose up


# Init the DB

init: 
	datacube system init
	datacube spindex create 3832
	datacube spindex update 3832

datacube-update-spindex:
	datacube spindex update 3832

# Indexing

products:
	dc-sync-products products-staging.csv --update-if-exists

index-dep-wofl:
	stac-to-dc \
		--catalog-href='https://stac.prod.digitalearthpacific.io' \
		--collections='dep_ls_wofl'

index-dep-wofs-annual:
	stac-to-dc \
		--catalog-href='https://stac.prod.digitalearthpacific.io' \
		--collections='dep_ls_wofs_summary_annual'

index-dep-wofs-alltime:
	stac-to-dc \
		--catalog-href='https://stac.prod.digitalearthpacific.io' \
		--collections='dep_ls_wofs_summary_alltime'

index-mangroves:
	stac-to-dc \
		--catalog-href='https://stac.staging.digitalearthpacific.io' \
		--collections='dep_s2_mangroves'

index-dep-s2-geomad:
	stac-to-dc \
		--catalog-href='https://stac.staging.digitalearthpacific.io' \
		--collections='dep_s2_geomad'

index-dep-s1-geomad:
	stac-to-dc \
		--catalog-href='https://stac.staging.digitalearthpacific.io' \
		--collections='dep_s1_geomad'

index-sentinel-2:
	stac-to-dc \
		--catalog-href='https://earth-search.aws.element84.com/v1' \
		--bbox='$(BIGBBOX)' \
		--datetime='2024-09-09' \
		--collections='sentinel-2-c1-l2a' \
		--limit=100
	# stac-to-dc \
	# 	--catalog-href='https://earth-search.aws.element84.com/v1' \
	# 	--bbox='$(BIGBBOX2)' \
	# 	--datetime='2024-09-9' \
	# 	--collections='sentinel-2-c1-l2a'

index-landsat-9:
	stac-to-dc \
		--catalog-href='https://earth-search.aws.element84.com/v1' \
		--bbox='$(BIGBBOX)' \
		--datetime='2024-09' \
		--collections='landsat-c2-l2' \
		--limit=100 \
		--options="query={\"platform\":{\"in\":[\"landsat-9\"]}}" \
		--rename-product=ls9_c2l2_sr


index-landsat-8:
	stac-to-dc \
		--catalog-href='https://earth-search.aws.element84.com/v1' \
		--bbox='$(BIGBBOX)' \
		--datetime='2024-09' \
		--collections='landsat-c2-l2' \
		--limit=100 \
		--options="query={\"platform\":{\"in\":[\"landsat-8\"]}}" \
		--rename-product=ls8_c2l2_sr

index-landsat-7:
	stac-to-dc \
		--catalog-href='https://earth-search.aws.element84.com/v1' \
		--bbox='$(BIGBBOX)' \
		--collections='landsat-c2-l2' \
		--limit=100 \
		--options="query={\"platform\":{\"in\":[\"landsat-7\"]}}" \
		--rename-product=ls7_c2l2_sr

index-landsat-5:
	stac-to-dc \
		--catalog-href='https://earth-search.aws.element84.com/v1' \
		--bbox='$(BIGBBOX)' \
		--collections='landsat-c2-l2' \
		--limit=100 \
		--options="query={\"platform\":{\"in\":[\"landsat-5\"]}}" \
		--rename-product=ls5_c2l2_sr

# OWS

ows-shell:
	docker-compose exec ows bash

ows-init:
	docker-compose exec ows \
		datacube-ows-update --schema --read-role dearth --write-role dearth

ows-update:
	docker-compose exec ows \
		bash -c " \
			datacube-ows-update --views && \
			datacube-ows-update \
		"

index-all: index-landsat-5 index-landsat-7 index-landsat-8 index-landsat-9 index-sentinel-1 index-sentinel-2 index-nasadem index-esri-lc

index-esri-lc:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--collections=io-lulc-9-class \
		--bbox=${BIGBBOX}
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--collections=io-lulc-9-class \
		--bbox=${BIGBBOX2}

index-nasadem:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--collections=nasadem \
		--bbox=${BIGBBOX}
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--collections=nasadem \
		--bbox=${BIGBBOX2}

index-sentinel-1:
	stac-to-dc \
		--catalog-href='https://planetarycomputer.microsoft.com/api/stac/v1/' \
		--bbox='$(BBOX)' \
		--datetime='2023-01-01/2023-12-31' \
		--collections='sentinel-1-rtc'

index-sentinel-1-pacific:
	stac-to-dc \
		--catalog-href='https://planetarycomputer.microsoft.com/api/stac/v1/' \
		--bbox='$(BIGBBOX)' \
		--datetime='2023-01-01/2023-12-31' \
		--collections='sentinel-1-rtc'
	stac-to-dc \
		--catalog-href='https://planetarycomputer.microsoft.com/api/stac/v1/' \
		--bbox='$(BIGBBOX2)' \
		--datetime='2023-01-01/2023-12-31' \
		--collections='sentinel-1-rtc'

