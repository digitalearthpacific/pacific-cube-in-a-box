from ows_config.common.ows_reslim_cfg import reslim_continental

style_mangroves = {
    "name": "mangroves",
    "title": "Mangroves",
    "abstract": "Mangroves",
    "needed_bands": ["mangroves"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mangroves",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#BDBDBD"},
        {"value": 1, "color": "#5ECC00"},
        {"value": 2, "color": "#3B7F00"},
    ],
    "legend": {},
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
        "default_style": "mangroves",
        "styles": [style_mangroves],
    },
}
