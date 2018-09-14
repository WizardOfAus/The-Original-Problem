#ipython magic numpy and matplotlib import function
%pylab inline 

#Step 1: Load Image
#Step 2: Display Image
#Step 3: Scale the image

#scale image between 0 and 1
im_scaled = im/255

#It's generally a good idea to get a feel for the distribution of data
fig = figure(0, (12,6))
hist(im_scaled.ravel(), 100); grid(1)

#Step 4: Convert to grayscale for more accuracy
def convert_to_grayscale(im):
    '''
    Convert color image to grayscale.
    Args: im = (nxmx3) floating point color image scaled between 0 and 1
    Returns: (nxm) floating point grayscale image scaled between 0 and 1
    '''
    return np.mean(im, axis = 2)

x = convert_to_grayscale(im_scaled)

#Step 5: Run
