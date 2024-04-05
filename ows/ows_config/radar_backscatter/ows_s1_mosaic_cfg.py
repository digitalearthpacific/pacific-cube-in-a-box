# From https://raw.githubusercontent.com/digitalearthafrica/config/master/services/ows_refactored/radar_backscatter/ows_sentinel1_cfg.py
from ows_config.common.ows_reslim_cfg import reslim_continental

style_vh_over_vv = {
    "name": "vv_vh_vh_over_vv",
    "title": "VV, VH and VH/VV",
    "abstract": "False colour representation of VV, VH and VH/VV for R, G and B respectively",
    "additional_bands": [],
    "components": {
        "red": {"mean_vv": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"mean_vh": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "mean_vh",
                "band2": "mean_vv",
                "scale_from": [0.0, 0.49],
            },
        },
    },
}


styles = {
    f"style{name}": {
        "name": name,
        "title": name.upper(),
        "abstract": f"{name} band",
        "additional_bands": [],
        "components": {
            "red": {name: 1.0, "scale_range": [0.0, 0.28]},
            "green": {name: 1.0, "scale_range": [0.0, 0.28]},
            "blue": {name: 1.0, "scale_range": [0.0, 0.28]},
        },
    }
    for name in ["mean_vv", "mean_vh", "std_vv", "std_vh", "median_vv", "median_vh"]
}


style_count = {
    "name": "count",
    "title": "Observation count",
    "abstract": "Count of observations included in median calculations",
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
        {"value": 10, "color": "#f3fabf"},
        {"value": 15, "color": "#e1f3b2"},
        {"value": 20, "color": "#c6e9b4"},
        {"value": 25, "color": "#97d6b9"},
        {"value": 30, "color": "#6bc6be"},
        {"value": 35, "color": "#42b6c4"},
        {"value": 40, "color": "#299dc1"},
        {"value": 45, "color": "#1f80b8"},
        {"value": 50, "color": "#225da8"},
        {"value": 60, "color": "#24419a"},
        {"value": 70, "color": "#1b2c80"},
        {"value": 80, "color": "#081d58"},
    ],
    "legend": {
        "begin": "0",
        "end": "80",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "80": {"suffix": "<"},
        },
    },
}


layer = {
    "title": "Sentinel-1 RTC Mosaic",
    "name": "dep_s1_mosaic",
    "abstract": """
todo...""",
    "product_name": "dep_s1_mosaic",
    "bands": {
        "mean_vv": [],
        "mean_vh": [],
        "std_vv": [],
        "std_vh": [],
        "median_vv": [],
        "median_vh": [],
        "count": [],
    },
    "dynamic": False,
    "resource_limits": reslim_continental,
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3832",
    "native_resolution": [10, -10],
    "styling": {
        "default_style": "vv_vh_vh_over_vv",
        "styles": [
            style_vh_over_vv,
            *styles.values(),
            style_count,
        ],
    },
}
