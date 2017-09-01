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


def create_image_batch_generator_function(data_dir, img_shape, pattern="*.jpg", shuffle=True):

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
