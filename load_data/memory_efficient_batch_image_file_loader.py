"""
A function that cretes an iterable *generator* object that traverses through
all the images in one single directory (in random order each time it is called).
"""
# TODO: make so it fetches the labels as well.
import numpy as np
import scipy
from scipy import misc
# from scipy.misc import imread
import glob
import os


# ==============================================================================
#                                          CREATE_IMAGE_BATCH_GENERATOR_FUNCTION
# ==============================================================================
def create_image_batch_generator_function(data_dir, img_shape, pattern="*.jpg", shuffle=True):
    """
    Creates a function that iteratively loads images from a directory in
    batches using a memory efficient *generator*. Ie, the images will
    only be loaded when needed so you do not need to store all the
    data on file at once.

    Args:
    - data_dir:  (str)
                 Path to the directory housing all the images.
    - img_shape: (tuple of integers)
                  What size should the images be resized to during
                  preprocessing.
    - pattern:    (str)(default="*.jpg")
                  Regex pattern to match only files in the directory that
                  match this pattern.

    Returns: (function)
    - Returns a function that has the following API:
        batch_generator(batch_size)

    Examples:
    For a directory containing 23 RGB images, loading in batches of 10, and
    resizing images to 100x100:

        >>> batch_generator = create_image_batch_generator_function(datadir, (100,100))
        >>> for batch in batch_generator(10):
        >>>     print(batch.shape)
        (10, 100, 100, 3)
        (10, 100, 100, 3)
        (3, 100, 100, 3)
    """

    def batch_generator(batch_size):
        """ A function that returns a generator object that can be iterated
            over. Simply specify the batch size.
        """
        # Randomly shuffle the order of the files in directory
        files = glob.glob(os.path.join(data_dir, pattern))
        np.random.shuffle(files)
        n_files = len(files)

        for batch_num in range(0, n_files, batch_size):
            batch = []

            for img_file in files[batch_num:batch_num+batch_size]:
                # Load image from file
                img = scipy.misc.imread(img_file)

                # -----------
                # BOOKMARK: File preprocessing steps here
                # -----------
                img = scipy.misc.imresize(img, img_shape)
                # -----------

                # Append to the batch
                batch.append(img)

            # Yield the current batch
            yield np.array(images)
    return batch_generator
