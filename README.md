# Kmean_resize_picture_P2
This code: purpose to resize a picture into small size using kmean
Talk a little bit a about how it work (via some steps below):
- First, we need to import and read an rgb value of a picture using some library (plt, image)
- Reshape it into (-1,3) because using kmean on sklearn, the form of data is (-1,3)
- Get the label of data via kmean, and the get the median value of all labels similarity
- All the label similarly'll get new value (median value of all values) --> new picture.
