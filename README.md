# Pacific Cube-in-a-Box

A simple example of the use of Microsoft Planetary Computer-hosted
data with the Open Data Cube.

## Getting started

Use the Makefile commands, or run the commands in them manually. You
need to have environment variables exported for connectivity to the
Postgres database too, which runs in Docker.

* Export environment variables:
``` bash
export DB_HOSTNAME=localhost
export DB_USERNAME=pacific
export DB_PASSWORD=secretpassword
export DB_DATABASE=odc
```
* Start the postgres DB: `make up` or `docker compose up`
* Add products: `make products` or `dc-sync-products products.csv`
* Index data individually or do it all with `make index-all`
* Now you can use any of the products. There's only one example notebook
  for now, for [Sentinel-1](notebooks/Sentinel1_Basic.ipynb).


## Next steps

Todo: get OWS and Explorer working as well a little Terria to visualise OWS
