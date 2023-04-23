"""
Image size for CNN. VGG16 must take in image size of 224, so that is hard-coded elsewhere.
"""
img_size = 48

"""
The number of facial emotion classes.
"""
num_classes = 7

"""
Number of training examples per batch.
"""
batch_size = 50

"""
Sample size for calculating the mean and standard deviation of the
training data. This many images will be randomly seleted to be read
into memory temporarily.
"""
preprocess_sample_size = 500