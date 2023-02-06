# I pledge my honor that I have abided by the Stevens Honor System.
# Haig Emirzian

import numpy as np
import cv2

#gets image from Desktop
image = cv2.imread("image.jpg")

#converts string to binary 
def convert(name):
    binary = ''
    for i in name:
        ascii_equivalent = ord(i)
        binary_equivalent = format(ascii_equivalent, '08b')
        binary += binary_equivalent
    return binary

bin_name = convert("Haig Emirzian")

#replace MSB bits
def replace_MSB(image, stego_key, bits):
    for i in range(len(bits)):
        bit = bits[i]
        a, b = stego_key[i]
        image[a][b] = (image[a][b] & 127) | (int(bit) << 7)
    return image

#stego key
stego_key = []
for i in range(min(len(bin_name), image.shape[0])):
    stego_key.append((i, i))

#replaces MSB with hidden binary encoding
result = replace_MSB(image, stego_key, bin_name)

#outputs "old" image
cv2.imwrite("MSB.jpg", result)
