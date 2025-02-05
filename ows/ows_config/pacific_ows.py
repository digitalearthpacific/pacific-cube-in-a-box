ows_cfg = {
    "global": {
        # Master config for all services and products.
        "response_headers": {
            "Access-Control-Allow-Origin": "*",  # CORS header
        },
        "services": {
            "wms": True,
            "wcs": True,
            "wmts": True,
        },
        "published_CRSs": {
            "EPSG:3857": {  # Web Mercator
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3577": {  # GDA-94, Australian Albers. Not sure why, but it's required!
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {"geographic": True, "vertical_coord_first": True},  # WGS-84
            "EPSG:3832": {  # Some Pacific projection
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
        },
        "allowed_urls": [
            "http://localhost:8000",
            "https://ows.staging.digitalearthpacific.io",
            "https://ows-uncached.staging.digitalearthpacific.io",
            "https://ows.prod.digitalearthpacific.io",
            "https://ows-uncached.prod.digitalearthpacific.io",
            "https://ows.digitalearthpacific.org",
        ],
        # Metadata to go straight into GetCapabilities documents
        "title": "Digital Earth Pacific Web Services",
        "abstract": """TODO...""",
        "info_url": "",
        "keywords": ["Digital Earth Pacific"],
        "contact_info": {
            "person": "TODO",
            "organisation": "Digital Earth Pacific",
            "position": "",
            "address": {
                "type": "postal",
                "address": "TODO",
                "city": "TODO",
                "state": "TODO",
                "postcode": "TODO",
                "country": "New Caledonia",
            },
            "telephone": "TODO",
            "fax": "",
            "email": "TODO",
        },
        "fees": "",
        "access_constraints": "TODO",
    },  # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        # "s3_aws_zone": "us-west-2",
        "max_width": 512,
        "max_height": 512,
        # Allow the WMS/WMTS GetCapabilities responses to be cached for 1 hour
        "caps_cache_maxage": 60 * 60,
    },  # END OF wms SECTION
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "formats": {
            "GeoTIFF": {
                # "renderer": "datacube_ows.wcs_utils.get_tiff",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_tiff",
                    "2": "datacube_ows.wcs2_utils.get_tiff",
                },
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False,
            },
            "netCDF": {
                # "renderer": "datacube_ows.wcs_utils.get_netcdf",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_netcdf",
                    "2": "datacube_ows.wcs2_utils.get_netcdf",
                },
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    },  # END OF wcs SECTION
    "layers": [
        {
            "title": "Digital Earth Pacific OWS",
            "abstract": "TODO",
            "layers": [
                # Hierarchical list of layers
                {
                    "title": "Earth Observation",
                    "abstract": """Earth Observation""",
                    "layers": [
                        {
                            "title": "Surface Reflectance",
                            "abstract": """Surface Reflectance""",
                            "layers": [
                                {
                                    "include": "ows_config.surface_reflectance.ows_s2_cfg.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_config.surface_reflectance.ows_landsat_cfg.layer_ls5",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_config.surface_reflectance.ows_landsat_cfg.layer_ls7",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_config.surface_reflectance.ows_landsat_cfg.layer_ls8",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_config.surface_reflectance.ows_landsat_cfg.layer_ls9",
                                    "type": "python",
                                },
                            ],
                        },
                        # {
                        #     "title": "Radar backscatter",
                        #     "abstract": """Radar backscatter""",
                        #     "layers": [
                        #         {
                        #             "include": "ows_config.radar_backscatter.ows_s1_cfg.layer",
                        #             "type": "python",
                        #         },
                        #     ],
                        # },
                        {
                            "title": "Annual Summary Products",
                            "abstract": """Annual Summary Products""",
                            "layers": [
                                # {
                                #     "include": "ows_config.surface_reflectance.ows_landsat_cfg.dep_ls_geomad",
                                #     "type": "python",
                                # },
                                {
                                    "include": "ows_config.surface_reflectance.ows_s2_cfg.dep_s2_geomad",
                                    "type": "python",
                                },
                                # {
                                #     "include": "ows_config.radar_backscatter.ows_s1_mosaic_cfg.layer",
                                #     "type": "python",
                                # },
                            ],
                        },
                    ],
                },
                # {
                #     "title": "Elevation",
                #     "abstract": """Digital elevation model""",
                #     "layers": [
                #         {
                #             "include": "ows_config.elevation.ows_nasadem_cfg.layer",
                #             "type": "python",
                #         },
                #     ],
                # },
                # {
                #     "title": "Land Cover",
                #     "abstract": """Land Cover""",
                #     "layers": [
                #         {
                #             "include": "ows_config.land_cover.ows_landcover.dep_s2s1_mrd_layer",
                #             "type": "python",
                #         },
                #     ],
                # },
            ],
        },
        {
            "title": "Surface water",
            "abstract": """Surface water""",
            "layers": [
                {
                    "title": "Daily surface water",
                    "abstract": """Daily surface water""",
                    "layers": [
                        {
                            "include": "ows_config.wofs.ows_wofl_ls_cfg.layer",
                            "type": "python",
                        },
                    ],
                },
                {
                    "title": "Annual surface water",
                    "abstract": """Annual surface water""",
                    "layers": [
                        {
                            "include": "ows_config.wofs.ows_wofs_annual_cfg.layer",
                            "type": "python",
                        },
                    ],
                },
            ],
        },
    ],
}
