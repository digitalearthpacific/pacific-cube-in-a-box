# Adapted from https://github.com/digitalearthafrica/config/blob/master/services/ows_refactored/wofs/ows_wofs_ls_cfg.py
from ows_config.common.ows_reslim_cfg import reslim_wofs_daily
from ows_config.wofs.band_wofs_cfg import bands_wofs_obs
from ows_config.wofs.style_wofs_ls import style_wofl_ls_obs, style_wofl_ls_wet

layer = {
    "title": "Water Observations from Space feature layer",
    "name": "dep_ls_wofl",
    "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all Pacific nations. The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally. Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water.

This product has a spatial resolution of 30 m and a temporal coverage of 1980s to current.

It is derived from Landsat Collection 2 surface reflectance product.

Daily water observations can be used to map historical flood and to understand surface water dynamics.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

""",
    "product_name": "dep_ls_wofl",
    "bands": bands_wofs_obs,
    "resource_limits": reslim_wofs_daily,
    "dynamic": True,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
        "always_fetch_bands": [],
        "manual_merge": False,
        "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
    },
    "flags": [
        {
            "band": "water",
            "product": "dep_ls_wofl",
            "ignore_time": False,
            "ignore_info_flags": [],
            "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
        },
    ],
    "native_crs": "EPSG:3857",
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "observations",
        "styles": [
            style_wofl_ls_obs,
            style_wofl_ls_wet,
        ],
    },
}
