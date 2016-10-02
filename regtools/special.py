import numpy as np
from skimage import transform
from skimage.feature import register_translation

from . import io


def _find_knobs_sem(sem_image, *, opening_radius=7, threshold=None):
    pass


def _sim_light_sem(sem_image, *,
                   opening_radius=7, threshold=None, blur_radius=40):
    pass


def _sim_light_dstorm(dstorm_image, *, blur_radius=40):
    pass


def register_rigid_cross_correlation(image, template):
    angles = np.linspace(0, 2 * np.pi, 360, endpoint=False)
    template_freq = np.fft.fftn(template)
    for angle in range(360):
        image_rot = transform.rotate(image, angle, resize=True,
                                     preserve_range=True)
        image_freq = np.fft.fftn(image_rot)
        shift, error, _ = register_translation(image_freq, template_freq,
                                               space='fourier')



def register_dstorm_to_sem(dstorm_image, sem_image):
    # Approach:
    # - preprocess sem_image to find knobs
    # - blur knobs with sigma = 40 (approx); potentially sigma = 500/res
    # - upscale dstorm image to match pixel size
    # - blur dstorm image with same sigma as sem image
    # - for each possible rotation of the dstorm image:
    #      - use register_translation to find appropriate transform
    #      - measure resulting cross-correlation
    # - choose rotation and translation giving best cross-correlation
    # - return aligned dstorm image and overlay
    pass