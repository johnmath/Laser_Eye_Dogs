# Nani_Dogs
This script uses a pretrained CNN from https://github.com/kairess/dog_face_detector to find dog's eyes and overlay laser eyes on them.

There are 2 command line arguments for this script: the image file path (--dog), and the size of the laser eyes as a float (--scale)

If the eyes are too big, try float values between 0 and 1 to shrink the laser eye size. If they are too small, use scale values larger than 1.

### Input:
![input](https://github.com/johna1020/Nani_Dogs/blob/master/example/input.jpg)

### Output:
![ouput](https://github.com/johna1020/Nani_Dogs/blob/master/example/nanidog.png)
