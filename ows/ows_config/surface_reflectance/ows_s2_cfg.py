from ows_config.common.ows_reslim_cfg import reslim_continental, reslim_sentinel2
from ows_config.surface_reflectance.band_sr_cfg import bands_s2_geomad, bands_sentinel2
from ows_config.surface_reflectance.style_sr_cfg import styles_s2_geomad, styles_s2_list

layer = {
    "title": "Sentinel-2 L2A",
    "name": "sentinel_2_c1_l2a",
    "abstract": """
TODO
""",
    "product_name": "sentinel_2_c1_l2a",
    "bands": bands_sentinel2,
    "dynamic": True,
    "resource_limits": reslim_sentinel2,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [10.0, -10.0],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_s2_list,
    },
}


dep_s2_geomad = {
    "title": "Annual GeoMAD (Sentinel-2)",
    "name": "dep_s2_geomad",
    "abstract": """
TODO
""",
    "product_name": "dep_s2_geomad",
    "bands": bands_s2_geomad,
    "dynamic": False,
    "resource_limits": reslim_continental,
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "ows_config.common.ows_util_tools.mask_by_emad_nan",
        "always_fetch_bands": ["emad"],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3832",
    "native_resolution": [10, -10],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_s2_geomad,
    },
}
