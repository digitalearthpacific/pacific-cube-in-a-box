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
            "value": 12.0,
            "color": "#90d743",
        },
        {
            "value": 20.0,
            "color": "#fde725",
        },
    ],
    "range": [0, 20],
    "legend": {
        "begin": "0",
        "end": "20",
        "ticks_every": "4",
        "units": "m",
        "tick_labels": {"20.0": {"label": "20+"}},
    },
}

confidence = {
    "name": "confidence",
    "title": "confidence",
    "abstract": "Vegetation height confidence",
    "needed_bands": ["confidence"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "confidence"},
    },
    # Grayscale: black (0) -> white (1)
    "color_ramp": [
        {"value": 0.0, "color": "#000000"},
        {"value": 0.2, "color": "#333333"},
        {"value": 0.4, "color": "#666666"},
        {"value": 0.6, "color": "#999999"},
        {"value": 0.8, "color": "#cccccc"},
        {"value": 1.0, "color": "#ffffff"},
    ],
    "range": [0.0, 1.0],
    "legend": {
        "begin": "0.0",
        "end": "1.0",
        "ticks_every": "0.2",
        "title": "Normalized Average Nearby Observations",
        "units": "",
    },
}

layer = {
    "name": "dep_s2_vegheight",
    "title": "Vegetation Height",
    "abstract": "Todo...",
    "product_name": "dep_s2_vegheight",
    "time_resolution": "summary",
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:3832",
    "native_resolution": [10, -10],
    "wcs": {},
    "bands": {
        "height": [],
        "confidence": [],
    },
    "styling": {
        "default_style": "height",
        "styles": [height, confidence],
    },
}
