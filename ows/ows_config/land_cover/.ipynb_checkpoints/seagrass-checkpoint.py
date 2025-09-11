from ows_config.common.ows_reslim_cfg import reslim_continental
import matplotlib.pyplot as plt
from datacube_ows.styles.api.base import apply_ows_style_cfg
from datacube_ows.styles.api.base import plot_image
import numpy as np

# Your style configuration from the previous file
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
    "valid_data_mask": [
        {
            "id": "nodata",
            "function": lambda data: data != 255,
            "bands": ["seagrass_probability"],
        },
    ],
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

def plot_image_with_transparent_background(cfg, data):
    """
    Plots an image from datacube-ows with a transparent background.
    """
    # Apply the OWS style to get the RGBA image
    styled_image = apply_ows_style_cfg(cfg, data)

    # Create a matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the styled image
    plot_image(styled_image, ax=ax)

    # Set the background of the axes to be transparent
    ax.set_facecolor("none")

    # Set the background of the figure to be transparent
    fig.patch.set_alpha(0.0)

    # Display the plot
    plt.show()

# Example usage (assuming 'probability' and 'data' are defined)
# plot_image_with_transparent_background(probability, data)



# def seagrass_nodata_mask(data):
#     """
#     A function to create a nodata mask.
#     Pixels with a value of 255 are considered nodata.
#     """
#     return data != 255

# probability = {
#     "name": "probability",
#     "title": "Probability",
#     "abstract": "Probability",
#     "needed_bands": ["seagrass_probability"],
#     "index_function": {
#         "function": "datacube_ows.band_utils.single_band",
#         "mapped_bands": True,
#         "kwargs": {
#             "band": "seagrass_probability",
#         },
#     },
#     "valid_data_mask": [
#         {
#             "id": "nodata",
#             "function": seagrass_nodata_mask,
#             "bands": ["seagrass_probability"],
#         },
#     ],
#     "color_ramp": [
#         {
#             "value": 0,
#             "color": "black",
#         },
#         {
#             "value": 1,
#             "color": "#010007",
#         },
#         {
#             "value": 10,
#             "color": "#170b3b",
#         },
#         {
#             "value": 20,
#             "color": "#410967",
#         },
#         {
#             "value": 30,
#             "color": "#6b176e",
#         },
#         {
#             "value": 40,
#             "color": "#952666",
#         },
#         {
#             "value": 50,
#             "color": "#bb3754",
#         },
#         {
#             "value": 60,
#             "color": "#dd5238",
#         },
#         {
#             "value": 70,
#             "color": "#f37719",
#         },
#         {
#             "value": 80,
#             "color": "#fba60b",
#         },
#         {
#             "value": 90,
#             "color": "#f5d948",
#         },
#         {
#             "value": 100,
#             "color": "#fcfea4",
#         },
#     ],
#     "range": [0, 100],
#     "legend": {
#         "begin": "0",
#         "end": "100",
#         "ticks_every": "20",
#     },
# }


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
                "title": "Nodata",
                "abstract": "No data",
                "values": [255],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Sediment",
                "abstract": "",
                "values": [1],
                "color": "#A3A3A3",
            },
            {
                "title": "Sand",
                "abstract": "",
                "values": [2],
                "color": "#FFDB0D",
            },
            {
                "title": "Rubble",
                "abstract": "",
                "values": [3],
                "color": "#FCFFD9",
            },
            {
                "title": "Seagrass",
                "abstract": "",
                "values": [4],
                "color": "#00FFD5",
            },
            {
                "title": "Algae",
                "abstract": "",
                "values": [5],
                "color": "#B2D11F",
            },
            {
                "title": "Coral",
                "abstract": "",
                "values": [6],
                "color": "#9322B3",
            },  # No 7 or 8 in the data
            {
                "title": "Rock",
                "abstract": "",
                "values": [7],
                "color": "#7A5300",
            },
            {
                "title": "Deeps",
                "abstract": "",
                "values": [8],
                "color": "#00057A",
            },
            {
                "title": "Mangrove",
                "abstract": "",
                "values": [9],
                "color": "#1D7869",
            },
            {
                "title": "Land",
                "abstract": "",
                "values": [10],
                "color": "#707070",
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
                "alpha": 0.0,
                "color": "#ffefa6",
            },
            {
                "title": "Seagrass",
                "abstract": "",
                "values": [1],
                "color": "#00FFD5",
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
                "alpha": 0.0,
                "color": "#ffefa6",
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
        "default_style": "seagrass",
        "styles": [seagrass, probability, classification, seagrass_60],
    },
}
