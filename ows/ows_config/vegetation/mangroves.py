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
    "abstract": "Mangrove percentage distribution using custom classification ranges",
    "needed_bands": ["mangroves"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mangroves",
        },
    },

    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 1.0},
        {"value": 10.0, "color": "#ffffcc"},
        {"value": 15.0, "color": "#c2e699"},
        {"value": 20.0, "color": "#a1d884"},  
        {"value": 25.0, "color": "#78c679"},
        {"value": 30.0, "color": "#41ab5d"},
        {"value": 40.0, "color": "#238443"},
        {"value": 60.0, "color": "#006837"},
        {"value": 100.0, "color": "#004529"},
        {"value": 255, "color": "#000000", "alpha": 1.0},
    ],

    "legend": {
        "width": 2.5,
        "height": 1.0,
        "ticks": [0, 25, 40, 60, 100],
        
"tick_labels": {
        "0": {"label": "0%"},
        "10": {"label": "10%"},
        "15": {"label": "15%"},
        "20": {"label": "20%"},
        "25": {"label": "25%"},
        "30": {"label": "30%"},
        "40": {"label": "40%"},
        "60": {"label": "60%"},
        "100": {"label": "100%"},
        },
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
        "default_style": "style_mangroves_percent",
        "styles": [style_mangroves_percent],
    },
}

