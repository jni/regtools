import os

import numpy as np
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


def test_incorrect_metadata_file_type():
    input_file = os.path.join(datadir, 'dstorm1.tif')
    assert_raises(ValueError, io.read_metadata_fei, input_file)


def test_imread_fei():
    sem_fn = os.path.join(datadir, 'sem1.tif')
    sem, semmd = io.imread_with_metadata(sem_fn)
    assert sem.dtype == 'uint16'
    assert_equal(np.max(sem), 65535)
    assert_equal(sem.shape, (1861, 2048))
    assert 'root' in semmd and 'Date' in semmd['root']


def test_imread_dstorm():
    dstorm_fn = os.path.join(datadir, 'dstorm1.tif')
    dstorm, dstormmd = io.imread_with_metadata(dstorm_fn)
    assert dstorm.dtype == 'float32'
    assert_approx_equal(np.max(dstorm), 940.35968, significant=6)
    assert_equal(dstorm.shape, (2048, 2048))
    assert 'x_resolution' in dstormmd
    assert_approx_equal(dstormmd['x_resolution'], 1e-8)
