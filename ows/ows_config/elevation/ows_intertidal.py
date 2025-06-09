from ows_config.common.ows_reslim_cfg import reslim_nasadem

style_elevation = {
    "name": "Elevation",
    "title": "Elevation",
    "abstract": "Elevation",
    "needed_bands": ["elevation"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "color_ramp": [
        {"value": -2.0, "color": "#e5f5e0"},  # Rare Subtidal
        {"value": -0.6, "color": "#c7e9c0"},  # Subtidal Edge
        {"value": -0.4, "color": "#a1d99b"},  # Dominant Range
        {"value": -0.2, "color": "#41ab5d"},  # Mid Intertidal
        {"value":  0.2, "color": "#78c679"},  # Upper Intertidal
        {"value":  1.0, "color": "#c2e699"},  # Supratidal
        {"value":  3.2, "color": "#f7fcb9"},  # High Supratidal
    ],
    "legend": {
        "title": "Elevation",
        "begin": "-2.0",
        "end": "3.2",
        "ticks_every": 0.5,
        "units": "m",
        "tick_labels": {
        "-2.0": {"label": "<"},
        "3.2": {"label": "+"}
        },
    },
}

style_exposure = {
    "name": "Exposure",
    "title": "Exposure",
    "abstract": "Exposure",
    "needed_bands": ["exposure"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "exposure",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#980043"},
        {"value": 20, "color": "#dd1c77"},
        {"value": 40, "color": "#df65b0"},
        {"value": 60, "color": "#c994c7"},
        {"value": 80, "color": "#d4b9da"},
        {"value": 100, "color": "#f1eef6"},
        # {"value": -0, "color": "#f1eef6", "alpha": 0.0},
    ],
    "legend": {
        "title": "Exposure",
        "begin": "0",
        "end": "100",
        "ticks_every": 20,
        "units": "%",
        "tick_labels": {
            "-1": {"prefix": "<"},
        },
    },
}

layer = {
    "title": "Intertidal",
    "name": "dep_s2ls_intertidal",
    "abstract": """
Todo...
""",
    "product_name": "dep_s2ls_intertidal",
    "time_resolution": "summary",
    "bands": {
        "elevation": [],
        "exposure": [],
    },
    "resource_limits": reslim_nasadem,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:3832",
    "native_resolution": [
        30,
        -30,
    ],
    "wcs": {},
    "styling": {
        "default_style": "Elevation",
        "styles": [style_elevation, style_exposure],
    },
}
