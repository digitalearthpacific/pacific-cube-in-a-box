from ows_config.common.ows_reslim_cfg import reslim_continental

probability = {
    "name": "probability",
    "title": "Probability",
    "abstract": "Probability",
    "needed_bands": ["seagrass_probability"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "seagrass_probability",
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
        {
            "value": 255,
            "color": "#fcfea4",
            "alpha": 1.0,
        },
    ],
    "range": [0, 100],
    "legend": {
        "begin": "0",
        "end": "100",
        "ticks_every": "20",
    },
}
  

classification = {
    "name": "classification",
    "title": "Classification",
    "abstract": "Coastal cover classification",
    "needed_bands": ["classification"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "classification",
        },
    },
    "value_map": {
        "classification": [
            {
                "title": "",
                "abstract": "",
                "values": [255],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Sediment",
                "abstract": "",
                "values": [1],
                "color": "#8c8c8c",
            },
            {
                "title": "Sand",
                "abstract": "",
                "values": [2],
                "color": "#fedd24",
            },
            {
                "title": "Rubble",
                "abstract": "",
                "values": [3],
                "color": "#f8ffb4",
            },
            {
                "title": "Seagrass",
                "abstract": "",
                "values": [4],
                "color": "#1acc44",
            },
            {
                "title": "Seaweed",
                "abstract": "",
                "values": [5],
                "color": "#df8e1c",
            },
            {
                "title": "Coral",
                "abstract": "",
                "values": [6],
                "color": "#a011c3",
            },  # No 7 or 8 in the data
            {
                "title": "Mangrove",
                "abstract": "",
                "values": [9],
                "color": "#086a39",
            },
            {
                "title": "Land",
                "abstract": "",
                "values": [10],
                "color": "#ffffff",
            },
            {
                "title": "Algae",
                "abstract": "",
                "values": [11],
                "color": "#b9df6f",
            },
            {
                "title": "Deeps",
                "abstract": "",
                "values": [12],
                "color": "#0435bc",
            },
            {
                "title": "Rock",
                "abstract": "",
                "values": [13],
                "color": "#535353",
            }
        ]
    },
    "legend": {"width": 3.0, "height": 3.0},
}

seagrass = {
    "name": "seagrass",
    "title": "Seagrass",
    "abstract": "Seagrass habitat",
    "needed_bands": ["seagrass"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "seagrass",
        },
    },
    "value_map": {
        "seagrass": [
            {
                "title": "",
                "abstract": "",
                "values": [255],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Not Seagrass",
                "abstract": "",
                "values": [0],
                "color": "#968640",
            },
            {
                "title": "Seagrass",
                "abstract": "",
                "values": [1],
                "color": "#1acc44",
            },
        ]
    },
}


seagrass_60 = {
    "name": "seagrass_60",
    "title": "Seagrass 60% Threshold",
    "abstract": "Seagrass habitat with 60% probability threshold",
    "needed_bands": ["seagrass_threshold_60"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "seagrass_threshold_60",
        },
    },
    "value_map": {
        "seagrass_threshold_60": [
            {
                "title": "",
                "abstract": "",
                "values": [255],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Not Seagrass",
                "abstract": "",
                "values": [0],
                "color": "#968640",
            },
            {
                "title": "Seagrass",
                "abstract": "",
                "values": [1],
                "color": "#1acc44",
            },
        ]
    },
}


seagrass_only = {
    "name": "seagrass",
    "title": "Seagrass",
    "abstract": "Seagrass habitat",
    "needed_bands": ["seagrass"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "seagrass",
        },
    },
    "value_map": {
        "seagrass": [
            {
                "title": "",
                "abstract": "",
                "values": [255],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Not Seagrass",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#968640",
            },
            {
                "title": "Seagrass",
                "abstract": "",
                "values": [1],
                "color": "#1acc44",
            },
        ]
    },
}



layer = {
    "title": "Seagrass detection",
    "name": "dep_s2_seagrass",
    "abstract": """
Todo...
""",
    "product_name": "dep_s2_seagrass",
    "time_resolution": "summary",
    "bands": {"classification": [], "seagrass": [], "seagrass_probability": [], "seagrass_threshold_60": []},
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
        "default_style": "seagrass_only",
        "styles": [seagrass_only, seagrass, probability, classification, seagrass_60],
    },
}
