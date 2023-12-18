from ows_config.common.ows_reslim_cfg import reslim_nasadem

bands_elevation = {
    "elevation": [],
}

style_greyscale = {
    "name": "greyscale",
    "title": "Greyscale",
    "abstract": "Greyscale elevation",
    "needed_bands": ["elevation"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#383838", "alpha": 0.0},
        {"value": 0.1, "color": "#383838"},
        {"value": 250, "color": "#5e5e5e"},
        {"value": 500, "color": "#858585"},
        {"value": 1000, "color": "#adadad"},
        {"value": 2000, "color": "#d4d4d4"},
        {"value": 4000, "color": "#fafafa"},
    ],
    "legend": {
        "title": "Elevation ",
        "begin": "0",
        "end": "4000",
        "ticks_every": 400,
        "units": "m",
        "tick_labels": {
            "4000": {"prefix": ">"},
        },
    },
}

style_colours = {
    "name": "colours",
    "title": "Coloured",
    "abstract": "Coloured elevation",
    "needed_bands": ["elevation"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#e1f2ff", "alpha": 0.0},
        {"value": 0.1, "color": "#41c23c"},
        {"value": 150, "color": "#f9a80e"},
        {"value": 300, "color": "#cb5f3e"},
        {"value": 400, "color": "#9d387d"},
        {"value": 500, "color": "#ba6daa"},
        {"value": 900, "color": "#d7a2d6"},
        {"value": 1200, "color": "#e6c8e6"},
        {"value": 4000, "color": "#ffecf9"},
    ],
    "legend": {
        "title": "Elevation ",
        "begin": "0",
        "end": "4000",
        "ticks_every": 400,
        "units": "m",
        "tick_labels": {
            "4000": {"prefix": ">"},
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
    "bands": bands_elevation,
    "resource_limits": reslim_nasadem,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000277777777780,
        -0.000277777777780,
    ],
    "wcs": {},
    "styling": {
        "default_style": "greyscale",
        "styles": [style_greyscale, style_colours],
    },
}
