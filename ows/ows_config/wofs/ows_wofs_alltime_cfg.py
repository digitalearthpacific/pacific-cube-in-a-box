from ows_config.common.ows_reslim_cfg import reslim_wofs
from ows_config.wofs.band_wofs_cfg import bands_wofs_summary
from ows_config.wofs.style_wofs_ls import (
    style_wofs_summary_alltime_frequency_masked,
    style_wofs_summary_alltime_frequency,
    style_wofs_summary_alltime_clear,
    style_wofs_summary_alltime_wet,
)

from ows_config.wofs.style_wofs_ls_legacy import (
    legacy_style_wofs_summary_alltime_frequency_masked,
    legacy_style_wofs_summary_alltime_frequency,
)


layer = {
    "title": "Water Observations from Space all time summary",
    "name": "wofs_ls_summary_alltime",
    "abstract": """
All-time water summary is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows what percentage of clear observations were detected as wet (ie. the ration of wet to clear as a percentage) from each calendar year.

This product has a spatial resolution of 30 m and a temporal coverage of 1980s to last calender year.

It is derived from Landsat Collection 2 surface reflectance product.

The all time summaries can be used to understand static patterns of water on the landscape.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003
""",
    "product_name": "dep_ls_wofs_summary_alltime",
    "time_resolution": "summary",
    "bands": bands_wofs_summary,
    "resource_limits": reslim_wofs,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:3832",
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "legacy_wofs_summary_alltime_frequency_masked",
        "styles": [
            legacy_style_wofs_summary_alltime_frequency_masked,
            style_wofs_summary_alltime_frequency_masked,
            legacy_style_wofs_summary_alltime_frequency,
            style_wofs_summary_alltime_frequency,
            style_wofs_summary_alltime_wet,
            style_wofs_summary_alltime_clear,
        ],
    },
}
