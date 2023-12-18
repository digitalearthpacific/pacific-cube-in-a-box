from ows_config.common.ows_reslim_cfg import reslim_sentinel2
from ows_config.surface_reflectance.band_sr_cfg import bands_sentinel2
from ows_config.surface_reflectance.style_sr_cfg import styles_s2_list

layer = {
    "title": "Sentinel-2 L2A",
    "name": "s2_l2a",
    "abstract": """
TODO
""",
    "product_name": "s2_l2a",
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
    "patch_url_function": "planetary_computer.sign_url",
}
