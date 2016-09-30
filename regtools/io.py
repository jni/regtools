import numpy as np

from skimage import io
from skimage.io._plugins.tifffile_plugin import TiffFile


def read_metadata_fei(filename):
    """Read the metadata from a TIFF produced by an FEI electron microscope.

    This metadata is included as ASCII text at the end of the file.

    Parameters
    ----------
    filename : str
        The input filename.

    Returns
    -------
    metadata : dict
        Dictionary of metadata.
    """
    md = {'root': {}}
    current_tag = 'root'
    reading_metadata = False
    with open(filename, 'rb') as fin:
        for line in fin:
            if not reading_metadata:
                if not line.startswith(b'Date='):
                    continue
                else:
                    reading_metadata = True
            line = line.rstrip().decode()
            if line.startswith('['):
                current_tag = line.lstrip('[').rstrip(']')
                md[current_tag] = {}
            else:
                if line and line != '\x00':  # ignore blank lines
                    key, val = line.split('=')
                    md[current_tag][key] = val
    return md


def read_metadata_tiff(filename):
    """Read *some* metadata contained in a TIFF file of a STORM image.

    This function should be considered very brittle, and currently only
    extracts the information I'm interested in, which is the pixel spacing,
    in meters.

    Parameters
    ----------
    filename : str
        The input filename.

    Returns
    -------
    md : dict
        Dictionary of metadata.
    """
    tif = TiffFile(filename)
    page = tif.pages[0]
    md = {'x_resolution': 1 / page.tags['x_resolution'].value[0]}
    tif.close()
    return md


def imread_with_metadata(filename, *, mdfunction=None):
    """Read a TIFF image with metadata.

    This reader attempts to auto-detect the metadata format. As with
    `read_metadata_tiff`, this function should be considered to be brittle.
    You can specify a Python function with which to read the metadata using
    the `mdfunction` keyword argument.

    Parameters
    ----------
    filename : str
        The input filename.
    mdfunction : callable, optional
        A function to read the metadata.

    Returns
    -------
    im : numpy array
        The image data.
    md : dict
        The metadata.
    """
    pass
