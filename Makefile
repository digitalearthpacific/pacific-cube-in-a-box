.PHONY: up products index-sentinel-1

# BBOX over Samoa and Tonga
BBOX := -180.0,-20.0,-170.0,-10.0

up:
	docker compose up

products:
	dc-sync-products products.csv

index-all: index-landsat-5 index-landsat-7 index-landsat-8 index-landsat-9 index-sentinel-1 index-sentinel-2 index-nasadem index-esri-lc

index-esri-lc:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--collections=io-lulc-9-class \
		--bbox=${BBOX}

index-nasadem:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--collections=nasadem \
		--bbox=${BBOX}

index-sentinel-1:
	stac-to-dc \
		--catalog-href='https://planetarycomputer.microsoft.com/api/stac/v1/' \
		--bbox='$(BBOX)' \
		--datetime='2023-01-01/2023-12-31' \
		--collections='sentinel-1-rtc'

index-sentinel-2:
	stac-to-dc \
		--catalog-href='https://planetarycomputer.microsoft.com/api/stac/v1/' \
		--bbox='$(BBOX)' \
		--datetime='2023-01-01/2023-12-31' \
		--collections='sentinel-2-l2a'

index-landsat-5:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--bbox=${BBOX} \
		--collections=landsat-c2-l2 \
		--options="query={\"platform\":{\"in\":[\"landsat-5\"]}}" \
		--rename-product=ls5_c2l2_sr

index-landsat-7:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--bbox=${BBOX} \
		--collections=landsat-c2-l2 \
		--options="query={\"platform\":{\"in\":[\"landsat-7\"]}}" \
		--rename-product=ls7_c2l2_sr

index-landsat-8:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--bbox=${BBOX} \
		--collections=landsat-c2-l2 \
		--options="query={\"platform\":{\"in\":[\"landsat-8\"]}}" \
		--rename-product=ls8_c2l2_sr

index-landsat-9:
	stac-to-dc \
		--catalog-href=https://planetarycomputer.microsoft.com/api/stac/v1/ \
		--bbox=${BBOX} \
		--collections=landsat-c2-l2 \
		--options="query={\"platform\":{\"in\":[\"landsat-9\"]}}" \
		--rename-product=ls9_c2l2_sr
