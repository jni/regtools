import os

from numpy.testing import assert_equal, assert_raises, assert_approx_equal

from regtools import io


rundir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(rundir, 'data')


def test_fei_metadata():
    md = io.read_metadata_fei(os.path.join(datadir, 'sem1.tif'))
    assert_equal(len(md), 18)
    assert 'root' in md
    assert 'Date' in md['root']
    assert_equal(md['root']['Date'], '08/02/2016')
    assert_approx_equal(float(md['Scan']['PixelHeight']), 5.39583e-9,
                        significant=6)


def test_tiff_metadata():
    md = io.read_metadata_tiff(os.path.join(datadir, 'dstorm1.tif'))
    assert 'x_resolution' in md
    assert_approx_equal(md['x_resolution'], 1e-8)
