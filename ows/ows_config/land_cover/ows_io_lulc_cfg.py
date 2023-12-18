from ows_config.common.ows_reslim_cfg import reslim_continental

bands_esri = {
    "data": [],
}

style_colours = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["data"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "data",
        },
    },
    "value_map": {
        "data": [
            {
                "title": "",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Water",
                "abstract": "",
                "values": [1],
                "color": "#419BDF",
            },
            {
                "title": "Trees",
                "abstract": "",
                "values": [2],
                "color": "#397D49",
            },
            {
                "title": "Grass",
                "abstract": "",
                "values": [3],
                "color": "#88B053",
            },
            {
                "title": "Flooded Vegetation",
                "abstract": "",
                "values": [4],
                "color": "#7A87C6",
            },
            {
                "title": "Crops",
                "abstract": "",
                "values": [5],
                "color": "#E49635",
            },
            {
                "title": "Scrub/Shrub",
                "abstract": "",
                "values": [6],
                "color": "#DFC35A",
            },
            {
                "title": "Built Area",
                "abstract": "",
                "values": [7],
                "color": "#C4281B",
            },
            {
                "title": "Bare Ground",
                "abstract": "",
                "values": [8],
                "color": "#A59B8F",
            },
            {
                "title": "Snow/Ice",
                "abstract": "",
                "values": [9],
                "color": "#A8EBFF",
            },
            {
                "title": "Clouds",
                "abstract": "",
                "values": [10],
                "color": "#616161",
            },
            {
                "title": "Rangeland",
                "abstract": "",
                "values": [11],
                "color": "#E3E2C3",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 3.0},
}

layer = {
    "title": "ESRI Land Use/Land Cover",
    "name": "esri_lulc",
    "abstract": """
Todo...
""",
    "product_name": "io_lulc",
    "time_resolution": "summary",
    "bands": bands_esri,
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [
        10.0,
        -10.0,
    ],
    "wcs": {},
    "styling": {
        "default_style": "style_colours",
        "styles": [style_colours],
    },
}

layer_9_class = {
    "title": "ESRI Land Use/Land Cover 9 Class",
    "name": "esri_lulc_9_class",
    "abstract": """
Todo...
""",
    "product_name": "io_lulc_9_class",
    "time_resolution": "summary",
    "bands": bands_esri,
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [
        10.0,
        -10.0,
    ],
    "wcs": {},
    "styling": {
        "default_style": "style_colours",
        "styles": [style_colours],
    },
}
