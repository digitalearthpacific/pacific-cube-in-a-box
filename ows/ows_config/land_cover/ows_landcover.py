from ows_config.common.ows_reslim_cfg import reslim_continental

style_proba = {
    "name": "proba",
    "title": "Probability",
    "abstract": "Probability",
    "needed_bands": ["proba"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "proba",
        },
    },
    "color_ramp": [
        {
            "value": 0,
            "color": "black",
        },
        {
            "value": 1,
            "color": "#010007",
        },
        {
            "value": 10,
            "color": "#170b3b",
        },
        {
            "value": 20,
            "color": "#410967",
        },
        {
            "value": 30,
            "color": "#6b176e",
        },
        {
            "value": 40,
            "color": "#952666",
        },
        {
            "value": 50,
            "color": "#bb3754",
        },
        {
            "value": 60,
            "color": "#dd5238",
        },
        {
            "value": 70,
            "color": "#f37719",
        },
        {
            "value": 80,
            "color": "#fba60b",
        },
        {
            "value": 90,
            "color": "#f5d948",
        },
        {
            "value": 100,
            "color": "#fcfea4",
        },
    ],
    "range": [0, 100],
    "legend": {
        "begin": "0",
        "end": "100",
        "ticks_every": "20",
    },
}


style_colours = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["class"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "class",
        },
    },
    "value_map": {
        "class": [
            {
                "title": "",
                "abstract": "",
                "values": [0],
                "alpha": 1.0,
                "color": "#707070",
            },
            {
                "title": "Bare Land",
                "abstract": "",
                "values": [1],
                "color": "#968640",
            },
            {
                "title": "Forest",
                "abstract": "",
                "values": [2],
                "color": "#064a00",
            },
            {
                "title": "Crops",
                "abstract": "",
                "values": [3],
                "color": "#ffce33",
            },
            {
                "title": "Grassland",
                "abstract": "",
                "values": [4],
                "color": "#d7ffa0",
            },
            {
                "title": "Settlements",
                "abstract": "",
                "values": [5],
                "color": "#b3b2ae",
            },
            {
                "title": "Mangroves",
                "abstract": "",
                "values": [6],
                "color": "#07b28d",
            },
            {
                "title": "Water",
                "abstract": "",
                "values": [7],
                "color": "#71a8ff",
            },
            {
                "title": "Quarry",
                "abstract": "",
                "values": [8],
                "color": "#b03a2e",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 3.0},
}

style_mud_and_gravel = {
    "name": "style_mud_and_gravel",
    "title": "Mineral Resource",
    "abstract": "Mineral resource extration",
    "needed_bands": ["class"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "class",
        },
    },
    "value_map": {
        "class": [
            {
                "title": "",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Bare Land",
                "abstract": "",
                "values": [1],
                "color": "#968640",
            },
            {
                "title": "Water",
                "abstract": "",
                "values": [7],
                "color": "#71a8ff",
            },
            {
                "title": "Quarry",
                "abstract": "",
                "values": [8],
                "color": "#b03a2e",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 3.0},
}

dep_s2s1_mrd_layer = {
    "title": "Mineral resource detection",
    "name": "dep_s2s1_mrd",
    "abstract": """
Todo...
""",
    "product_name": "dep_s2s1_mrd",
    "time_resolution": "summary",
    "bands": {"class": [], "proba": []},
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
        "default_style": "style_mud_and_gravel",
        "styles": [style_mud_and_gravel, style_proba, style_colours],
    },
}
