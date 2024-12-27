from ows_config.common.ows_reslim_cfg import reslim_continental, reslim_landsat
from ows_config.surface_reflectance.band_sr_cfg import (
    bands_ls5_7_sr,
    bands_ls8_9_sr,
    bands_ls_geomad,
)
from ows_config.surface_reflectance.style_sr_cfg import (
    styles_landsat_5_7,
    styles_landsat_8_9,
    styles_ls_geomad,
)

dep_ls_geomad = {
    "title": "Annual GeoMAD (Landsat 8 & 9)",
    "name": "dep_ls_geomad",
    "abstract": """
TODO
""",
    "product_name": "dep_ls_geomad",
    # "low_res_product_name": "gm_ls8_ls9_annual_lowres",  # todo...
    "bands": bands_ls_geomad,
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
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_ls_geomad,
    },
}

layer_ls5 = {
    "title": "Landsat 5 C2L2",
    "name": "ls5_c2l2_sr",
    "abstract": """
TODO""",
    "product_name": "ls5_c2l2_sr",
    "bands": bands_ls5_7_sr,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_landsat_5_7,
    },
}

layer_ls7 = {
    "title": "Landsat 7 C2L2",
    "name": "ls7_c2l2_sr",
    "abstract": """
TODO""",
    "product_name": "ls7_c2l2_sr",
    "bands": bands_ls5_7_sr,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_landsat_5_7,
    },
}

layer_ls8 = {
    "title": "Landsat 8 C2L2",
    "name": "ls8_c2l2_sr",
    "abstract": """
TODO""",
    "product_name": "ls8_c2l2_sr",
    "bands": bands_ls8_9_sr,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_landsat_8_9,
    },
}

layer_ls9 = {
    "title": "Landsat 9 C2L2",
    "name": "ls9_c2l2_sr",
    "abstract": """
TODO""",
    "product_name": "ls9_c2l2_sr",
    "bands": bands_ls8_9_sr,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3857",
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_landsat_8_9,
    },
}
