from ows_config.common.ows_reslim_cfg import reslim_nasadem

style_blues_depth = {
    "name": "blues_depth",
    "title": "Blues (Depth)",
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
        {"value": -16.0, "color": "#034e7b"},
        {"value": -8.0, "color": "#0570b0"},
        {"value": -6.0, "color": "#3690c0"},
        {"value": -4.0, "color": "#74a9cf"},
        {"value": -3.0, "color": "#a6bddb"},
        {"value": -2.0, "color": "#d0d1e6"},
        {"value": -1.0, "color": "#f1eef6"},
        {"value": -0, "color": "#f1eef6", "alpha": 0.0},
    ],
    "legend": {
        "title": "Depth ",
        "begin": "-16",
        "end": "0",
        "ticks_every": 2,
        "units": "m",
        "tick_labels": {
            "-16": {"prefix": "<"},
        },
    },
}

style_blues_mean = {
    "name": "blues_mean",
    "title": "Blues (Mean)",
    "abstract": "Blue mean",
    "needed_bands": ["mean"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean",
        },
    },
    "color_ramp": [
        {"value": -16.0, "color": "#034e7b"},
        {"value": -8.0, "color": "#0570b0"},
        {"value": -6.0, "color": "#3690c0"},
        {"value": -4.0, "color": "#74a9cf"},
        {"value": -3.0, "color": "#a6bddb"},
        {"value": -2.0, "color": "#d0d1e6"},
        {"value": -1.0, "color": "#f1eef6"},
        {"value": -0, "color": "#f1eef6", "alpha": 0.0},
    ],
    "legend": {
        "title": " Depth ",
        "begin": "-16",
        "end": "0",
        "ticks_every": 2,
        "units": "m",
        "tick_labels": {
            "-16": {"prefix": "<"},
        },
    },
}

style_blues_median = {
    "name": "blues_median",
    "title": "Blues (Median)",
    "abstract": "Blue median",
    "needed_bands": ["median"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "median",
        },
    },
    "color_ramp": [
        {"value": -16.0, "color": "#034e7b"},
        {"value": -8.0, "color": "#0570b0"},
        {"value": -6.0, "color": "#3690c0"},
        {"value": -4.0, "color": "#74a9cf"},
        {"value": -3.0, "color": "#a6bddb"},
        {"value": -2.0, "color": "#d0d1e6"},
        {"value": -1.0, "color": "#f1eef6"},
        {"value": -0, "color": "#f1eef6", "alpha": 0.0},
    ],
    "legend": {
        "title": " Depth ",
        "begin": "-16",
        "end": "0",
        "ticks_every": 2,
        "units": "m",
        "tick_labels": {
            "-16": {"prefix": "<"},
        },
    },
}

style_count_sdb = {
    "name": "count",
    "title": "Prediction count",
    "abstract": "Count of observations included in sdb depth predictions",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count",
        },
    },
    "needed_bands": ["count"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#FFFFFF",
            "alpha": 1,
        },
        {"value": 5, "color": "#f3fabf"},
        {"value": 10, "color": "#e1f3b2"},
        {"value": 15, "color": "#c6e9b4"},
        {"value": 20, "color": "#97d6b9"},
        {"value": 25, "color": "#6bc6be"},
        {"value": 30, "color": "#42b6c4"},
        {"value": 35, "color": "#299dc1"},
        {"value": 40, "color": "#1f80b8"},
        {"value": 45, "color": "#225da8"},
        {"value": 50, "color": "#24419a"},
    ],
    "legend": {
        "begin": "0",
        "end": "50",
        "decimal_places": 0,
        "ticks_every": 10,
        "tick_labels": {
            "50": {"suffix": "<"},
        },
    },
}

style_pc_prediction = {
    "name": "percentage_prediction",
    "title": "Percentage Prediction",
    "abstract": "Percentage Prediction",
    "needed_bands": ["pc_pred"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pc_pred",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {"value": 0.01, "color": "#f2f0f7"},
        {"value": 0.2, "color": "#dadaeb"},
        {"value": 0.4, "color": "#bcbddc"},
        {"value": 0.6, "color": "#9e9ac8"},
        {"value": 0.8, "color": "#756bb1"},
        {"value": 1.0, "color": "#54278f"},
    ],
    "legend": {
        "title": "Percentage Prediction",
        "begin": "0",
        "end": "1",
        "ticks_every": 0.2,
        "units": "%",
    },
}

style_pc_deep = {
    "name": "percentage_deep",
    "title": "Percentage Deep",
    "abstract": "Percentage Deep",
    "needed_bands": ["pc_deep"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pc_deep",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {"value": 0.01, "color": "#f2f0f7"},
        {"value": 0.2, "color": "#dadaeb"},
        {"value": 0.4, "color": "#bcbddc"},
        {"value": 0.6, "color": "#9e9ac8"},
        {"value": 0.8, "color": "#756bb1"},
        {"value": 0.99, "color": "#54278f"},
        {"value": 1, "color": "#666666", "alpha": 0},
    ],
    "legend": {
        "title": "Percentage Deep",
        "begin": "0",
        "end": "1",
        "ticks_every": 0.2,
        "units": "%",
    },
}

style_stdev = {
    "name": "standard_deviation",
    "title": "Standard Deviation",
    "abstract": "Standard Deviation",
    "needed_bands": ["stdev"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stdev",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#ffffe5"},
        {"value": 1.0, "color": "#fff7bc"},
        {"value": 1.5, "color": "#fee391"},
        {"value": 2.0, "color": "#fec44f"},
        {"value":  2.5, "color": "#fe9929"},
        {"value":  3.0, "color": "#ec7014"},
        {"value":  6.0, "color": "#cc4c02"},
        {"value":  9.0, "color": "#993404"},
        {"value":  12.0, "color": "#662506"},
    ],
    "legend": {
    "title": "Standard Deviation",
    "begin": "0",
    "end": "12.0",
    "ticks_every": 0.5,
    "units": "m",
    "tick_labels": {
        "12": {"suffix": "+"}
    }
}
}

layer = {
    "title": "SDB",
    "name": "sdb",
    "abstract": """
Todo...
""",
    "product_name": "dep_s2_sdb",
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
        "default_style": "blues_depth",
        "styles": [style_blues_depth, style_blues_mean, style_blues_median, style_count_sdb, style_pc_prediction, style_pc_deep, style_stdev],
    },
}
