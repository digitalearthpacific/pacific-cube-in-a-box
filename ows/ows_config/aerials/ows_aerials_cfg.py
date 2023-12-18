layer = {
    "title": "Aerial Imagery RGB",
    "name": "aerial_rgb",
    "abstract": """
TODO
""",
    "product_name": "airborne_rgb",
    "time_resolution": "day",
    "bands": {
        "red": [],
        "green": [],
        "blue": []
    },
    "resource_limits": {
        "wms": {
            "zoomed_out_fill_colour": [150, 180, 200, 160],
            "min_zoom_factor": 35.0,
        },
        "wcs": {}
    },
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [0.1677696917139964439, -0.1677696917139964439],
    "wcs": {},
    "styling": {
        "default_style": "simple_rgb",
        "styles": [
            {
                "name": "simple_rgb",
                "title": "Simple RGB",
                "abstract": "Simple true-colour image, using the red, green and blue bands",
                "components": {"red": {"red": 1.0}, "green": {"green": 1.0}, "blue": {"blue": 1.0}},
                "scale_range": [0.0, 255.0],
            },
            {
                "name": "red",
                "title": "Red",
                "abstract": "Red band",
                "components": {"red": {"red": 1.0}, "green": {"red": 1.0}, "blue": {"red": 1.0}},
                "scale_range": [0, 255],
            },
            {
                "name": "green",
                "title": "Green",
                "abstract": "Green band",
                "components": {"red": {"green": 1.0}, "green": {"green": 1.0}, "blue": {"green": 1.0}},
                "scale_range": [0, 255],
            },
            {
                "name": "blue",
                "title": "Blue",
                "abstract": "Blue band",
                "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
                "scale_range": [0, 255],
            }
        ],
    },
}
