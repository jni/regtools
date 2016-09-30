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
