from ows_config.common.ows_reslim_cfg import reslim_nasadem


style_blues = {
    "name": "blues",
    "title": "Blues",
    "abstract": "Blue depth",
    "needed_bands": ["depth"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "depth",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#f1eef6", "alpha": 0.0},
        {"value": -0.1, "color": "#f1eef6"},
        {"value": -1.0, "color": "#d0d1e6"},
        {"value": -2.0, "color": "#a6bddb"},
        {"value": -4.0, "color": "#74a9cf"},
        {"value": -8.0, "color": "#3690c0"},
        {"value": -16.0, "color": "#0570b0"},
        {"value": -32.0, "color": "#034e7b"},
    ],
    "legend": {
        "title": "Depth ",
        "begin": "0",
        "end": "-20",
        "ticks_every": 2,
        "units": "m",
        "tick_labels": {
            "-32": {"prefix": "<"},
        },
    },
}


style_greyscale = {
    "name": "greyscale",
    "title": "Greyscale",
    "abstract": "Greyscale depth",
    "needed_bands": ["depth"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "depth",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#0000FF", "alpha": 0.0},
        {"value": -0.1, "color": "#0000CC"},
        {"value": -1.0, "color": "#000099"},
        {"value": -2.0, "color": "#000066"},
        {"value": -4.0, "color": "#000033"},
        {"value": -8.0, "color": "#000022"},
        {"value": -16.0, "color": "#000011"},
        {"value": -32.0, "color": "#000000"},
    ],
    "legend": {
        "title": "Depth ",
        "begin": "0",
        "end": "-20",
        "ticks_every": 2,
        "units": "m",
        "tick_labels": {
            "-32": {"prefix": "<"},
        },
    },
}

layer = {
    "title": "NASADEM",
    "name": "nasadem",
    "abstract": """
Todo...
""",
    "product_name": "nasadem",
    "time_resolution": "summary",
    "bands": {
        "depth": [],
    },
    "resource_limits": reslim_nasadem,
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
        "default_style": "blues",
        "styles": [style_greyscale, style_blues],
    },
}
