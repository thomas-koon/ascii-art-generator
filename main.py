import PIL
import numpy
from PIL import Image

#the image we are using
image = Image.open("test_image.jpg")

image.show()
print("Image size: " + str(image.width) + " x " + str(image.height))

pixel_matrix = numpy.array(image)
# each of the 67-3 characters that can be printed
all_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
#print(pixel_matrix)
for x in pixel_matrix:
    char_width_so_far = 0
    for y in x:
        rgb = y
        # print("rgb: " + str(rgb))
        # the brightness value of the current pixel, based on rgb
        brightness = numpy.average(rgb)
        a = 0
        position_of_character_in_all_characters = 0
        count = 0
        # we keep adding 3.8 (255/67) to a until the brightness is greater than a.
        # we also keep incrementing count by 1
        # when brightness is finally larger than a, we know how many times 3.8 goes into
        # the brightness value. this number, shown by count, will be the place in
        # all_characters that represents the brightness value
        while brightness >= a:
            a = a + (256/65)
            count = count + 1
        # print("count " + str(count))
        char = all_characters[count-1]
        # how many characters have been printed to the same line so far
        char_width_so_far = 0
        if char_width_so_far == 0:
            print(char*3, end='')
        elif char_width_so_far == len(x)-1:
            print("\n"+(char*3), end='')
        else:
            print(char*3, end='')
        char_width_so_far += 1
    image.close()


			