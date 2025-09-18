from ows_config.common.ows_reslim_cfg import reslim_continental

height = {
    "name": "height",
    "title": "height",
    "abstract": "Vegetation height",
    "needed_bands": ["height"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "height",
        },
    },
    "color_ramp": [
        {
            "value": 0,
            "alpha": 0.0,
            "color": "black",
        },
        {
            "value": 0.1,
            "color": "#440154",
        },
        {
            "value": 1.5,
            "color": "#443983",
        },
        {
            "value": 3.0,
            "color": "#31688e",
        },
        {
            "value": 4.5,
            "color": "#21918c",
        },
        {
            "value": 6.0,
            "color": "#35b779",
        },
        {
            "value": 18.0,
            "color": "#90d743",
        },
        {
            "value": 40.0,
            "color": "#fde725",
        },
    ],
    "range": [0, 40],
    "legend": {
        "begin": "0",
        "end": "40",
        "ticks_every": "8",
    },
}


layer = {
    "title": "Vegetation Height",
    "name": "dep_s2_vegheight",
    "abstract": """
Todo...
""",
    "product_name": "dep_s2_vegheight",
    "time_resolution": "summary",
    "bands": {"height": [],},
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:3832",
    "native_resolution": [
        10,
        -10,
    ],
    "wcs": {},
    "styling": {
        "default_style": "height",
        "styles": [height],
    },
}
