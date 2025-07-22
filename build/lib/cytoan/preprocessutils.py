import cv2
import numpy as np  

def channel_select(image: np.ndarray, channel_indicies: list) -> np.ndarray:
	"""
    Select or zero out specified channels of an input image.

    This function returns a copy of the input image where channels corresponding to 0 in
    `channel_indicies` are zeroed out, and channels corresponding to 1 are kept unchanged.

    Parameters
    ----------
    image : numpy.ndarray
        Input image array with shape (height, width, channels). Must be a 3D array.
    channel_indicies : list of int
        List of integers (0 or 1), with length equal to the number of channels in the image.
        A 1 indicates that channel is kept; 0 means the channel is zeroed out.

    Returns
    -------
    numpy.ndarray
        A copy of the input image with specified channels zeroed out.

    Raises
    ------
    ValueError
        If `channel_indicies` contains all zeros.
        If the number of channels in `image` does not match the length of `channel_indicies`.
        If the input image has only one channel (grayscale).

    Examples
    --------
    >>> import cv2
    >>> img = cv2.imread('image.jpg')
    >>> result = channel_select(img, [0, 1, 1])  # zero out blue channel if image is BGR
    """

	output_img = image.copy()

	if list and all(x == 0 for x in channel_indicies):
		raise ValueError("At least one channel must have a nonzero value to produce a result.")

	if image.ndim == 2:
		channels = 1
	else: 
		channels = image.shape[2]

	if channels != len(channel_indicies):
		raise ValueError(f"Image has {channels} channels but channel_indicies has {len(channel_indicies)} items.")

	mask = np.array(channel_indicies, dtype=bool)

	if channels == 1:
		raise ValueError("Image has 1 channel so channel selection cannot occur.")
	else:
		for ch in range(channels):
			if not mask[ch]:
				output_img[:, :, ch] = 0

	return output_img

