from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd

import scattermap  # source obtained from: https://gist.github.com/lukauskas/f2f43aad6078a8b5d71b986174487b8c


SETTINGS = {
    # INPUT FILE SETTINGS
    # Write the input Excel file and sheet name here.
    'input_file': 'sample_data.xlsx',
    'sheet_name': 'sample_data',

    # PLOT SETTINGS
    # Select plot size in inches. This is used when saving the plot as a file.
    'width': 8,
    'height': 8,

    # MASK SETTINGS
    # Whether to show/hide values that do not represent a significant clinical outcome (+- 1.86 SD).
    'mask_non_significant_values': True,

    # COLORMAP SETTINGS
    # Select which colormap to use, and how to calculate its min/max values (color does not change beyond these values).
    # Use None to calculate min/center/max values directly from dataset.
    # For divergent colormaps, a center of 0.0 is recommended.
    # more colormap names at: https://matplotlib.org/stable/tutorials/colors/colormaps.html#miscellaneous
    'colormap_name': 'RdBu',
    'colormap_min_value': None,
    'colormap_center': 0.0,
    'colormap_max_value': None,

    # MARKER SETTINGS
    # Select the size and edge width of the markers (circles).
    'marker_size': 500.0,
    'linewidths': 2.0,

    # OUTPUT SETTINGS
    # Select a desired output file name and format.
    # Some available formats:
    # - png (a regular image)
    # - pdf (PDF file)
    # - svg (vector graphics for Illustrator, Inkscape etc)
    'output_file': 'result',
    'output_format': 'png',
}


def main(
    input_file: str,
    sheet_name: str,
    width: int,
    height: int,
    mask_non_significant_values: bool,
    colormap_name: str,
    colormap_min_value: Optional[float],
    colormap_center: Optional[float],
    colormap_max_value: Optional[float],
    marker_size: Optional[float],
    linewidths: Optional[float],
    output_file: str,
    output_format: str,
) -> None:
    """Main function of this script."""
    # Loads input data
    data = pd.read_excel(
        input_file,
        sheet_name=sheet_name,
        index_col=0,
        header=[0, 1]
    ).T

    # Gets mask values (if user chose to do so)
    mask = data.abs() < 1.86 if mask_non_significant_values is True else None

    # Draws data onto plot
    fig, ax = plt.subplots(figsize=(width, height))
    scattermap.scattermap(
        ax=ax,
        data=data,
        cmap=colormap_name,
        vmin=colormap_min_value,
        vmax=colormap_max_value,
        center=colormap_center,
        marker_size=marker_size,
        linewidths=linewidths,
        mask=mask,
        linecolor='black',
        robust=True,
        xticklabels=1,
        yticklabels=1,
    )

    # Sets XY axis labels
    ax.set_xlabel('Patient ID')
    ax.set_ylabel('Variable')

    # Fixes Y tick labels
    labels = [' - '.join(list(t)) for t in data.index]
    ax.set_yticklabels(labels)

    # Displays plot
    plt.tight_layout()
    plt.show()

    # Saves to output image (if user chose to do so)
    if output_file:
        image_path = f'{output_file}.{output_format.lower()}'
        fig.savefig(image_path)


if __name__ == '__main__':
    main(**SETTINGS)
