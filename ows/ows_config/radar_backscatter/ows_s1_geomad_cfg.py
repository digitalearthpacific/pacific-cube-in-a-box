# From https://raw.githubusercontent.com/digitalearthafrica/config/master/services/ows_refactored/radar_backscatter/ows_sentinel1_cfg.py
from ows_config.common.ows_reslim_cfg import reslim_continental

style_vh_over_vv = {
    "name": "vv_vh_vh_over_vv",
    "title": "VV, VH and VH/VV",
    "abstract": "False colour representation of VV, VH and VH/VV for R, G and B respectively",
    "additional_bands": [],
    "components": {
        "red": {"vv": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"vh": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "vh",
                "band2": "vv",
                "scale_from": [0.0, 0.49],
            },
        },
    },
}


styles = {
    f"style_{name}": {
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
    for name in ["vv", "vh", "stdev_vv", "stdev_vh", "vv", "vh"]
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

smad_scaling = [0.00, 0.10]
emad_scaling = [0.00, 0.10]
bcmad_scaling = [0.00, 0.2]

style_smad_std = {
    "name": "arcsec_smad",
    "title": "Spectral MAD (SMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_arcsec",
        "mapped_bands": True,
        "kwargs": {"band": "smad", "scale_from": smad_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["smad"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nSMAD"},
            "4.0": {"label": "High\nSMAD"},
        },
    },
}

style_emad_std = {
    "name": "log_emad",
    "title": "Euclidean MAD (EMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "emad", "scale_from": emad_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["emad"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nEMAD"},
            "4.0": {"label": "High\nEMAD"},
        },
    },
}


style_bcmad_std = {
    "name": "log_bcmad",
    "title": "Bray-Curtis MAD (BCMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {
            "band": "bcmad",
            "scale_from": bcmad_scaling,
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["bcmad"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nBCMAD"},
            "4.0": {"label": "High\nBCMAD"},
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
        "vv": [],
        "vh": [],
        "stdev_vv": [],
        "stdev_vh": [],
        "mean_vv": [],
        "mean_vh": [],
        "bcmad": [],
        "smad": [],
        "emad": [],
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
            style_smad_std,
            style_emad_std,
            style_bcmad_std,
        ],
    },
}
