from ows_config.common.ows_reslim_cfg import reslim_continental

style_mangroves = {
    "name": "style_mangroves",
    "title": "Mangrove Cover",
    "abstract": "Mangrove Cover",
    "needed_bands": ["mangroves"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mangroves",
        },
    },
    "value_map": {
        "mangroves": [
            {
                "title": "No Mangroves",
                "abstract": "",
                "values": [0],
                "alpha": 1.0,
                "color": "#BDBDBD",
            },
            {
                "title": "Open Mangroves",
                "abstract": "",
                "values": [1],
                "color": "#5ECC00",
            },
            {
                "title": "Closed Mangroves",
                "abstract": "",
                "values": [2],
                "color": "#3B7F00",
            }
        ]
    },
    "legend": {"width": 2.5, "height": 1.0},
}

style_mangroves_alt = {
    "name": "style_mangroves_alt",
    "title": "Mangrove Cover",
    "abstract": "Mangrove Cover",
    "needed_bands": ["mangroves"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mangroves",
        },
    },
    "value_map": {
        "mangroves": [
            {
                "title": "No Mangroves",
                "abstract": "",
                "values": [0],
                "alpha": 1.0,
                "color": "#BDBDBD",
            },
            {
                "title": "Open Mangroves",
                "abstract": "",
                "values": [1],
                "color": "#A15EFF",
            },
            {
                "title": "Closed Mangroves",
                "abstract": "",
                "values": [2],
                "color": "#5E2B97",
            }
        ]
    },
    "legend": {"width": 2.5, "height": 1.0},
}



style_mangroves_percent = {
    "name": "style_mangroves_percent",
    "title": "Mangrove Distribution (%)",
    "abstract": "Mangrove percentage distriution using custom classification ranges",
    "needed_bands": ["mangroves"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mangroves",
        },
    },
    "value_map": {
        "mangroves": [
            {
                "title": "<10%",
                "abstract": "",
                "range": [0.0, 10.0],
                "color": "#ffffcc",
            },
            {
                "title": "10–15%",
                "abstract": "",
                "range": [10.0, 15.0],
                "color": "#c2e699",
            },
            {
                "title": "20–25%",
                "abstract": "",
                "range": [20.0, 25.0],
                "color": "#78c679",
            },
            {
                "title": "25–30%",
                "abstract": "",
                "range": [25.0, 30.0],
                "color": "#41ab5d",
            },
            {
                "title": "30–40%",
                "abstract": "",
                "range": [30.0, 40.0],
                "color": "#238443",
            },
            {
                "title": "40–60%",
                "abstract": "",
                "range": [40.0, 60.0],
                "color": "#006837",
            },
            {
                "title": "60–100%",
                "abstract": "",
                "range": [60.0, 100.0],
                "color": "#004529",
            },
        ]
    },
    "legend": {
        "width": 2.5,
        "height": 1.0,
        "ticks": False,
        "tick_labels": True,
        "units": "%",
    },
}


layer = {
    "title": "Mangroves",
    "name": "mangroves",
    "abstract": """
Todo...
""",
    "product_name": "dep_s2_mangroves",
    "time_resolution": "summary",
    "bands": {"mangroves": []},
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
        "default_style": "style_mangroves",
        "styles": [style_mangroves, style_mangroves_alt],
    },
}

