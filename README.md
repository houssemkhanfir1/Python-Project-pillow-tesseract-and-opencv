
# Pillow Project

This project will take us through the process of processing images using the Python Library Image PIL. 

this program is going to going to change the colors of the image, creating variations based on a single photo. There are many complex ways to change a photograph using variations, such as changing a black and white image to either "cool" variants, which have light purple and blues in them, or "warm" variants, which have touches of yellow and may look sepia toned. This code will  be just changing the image one color channel at a time.

From the image you can see there are two parameters which are being varied for each sub-image. First, the rows are changed by color channel, where the top is the red channel, the middle is the green channel, and the bottom is the blue channel. Wait, why don't the colors look more red, green, and blue, in that order? Because the change you to be making is the ratio, or intensity, or that channel, in relationship to the other channels. We're going to use three different intensities, 0.2 (reduce the channel a lot), 0.4 (reduce the channel approximatly to half), and 0.7 (reduce the channel only a little bit).

For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. So the top row of changes would create three alternative pixels, varying the first channel (red). one at (20, 100, 50), one at (100, 100, 50), and one at (180, 100, 50). The next row would vary the second channel (blue), and would create pixels of color values (200, 10, 50), (200, 50, 50) and (200, 90, 50).

## Notes

A font is included for your usage if you would like! It's located in the file "readonly/fanwood-webfont.ttf"

Check out the PIL.ImageDraw module for helpful functions.

Check out the PIL.ImageFont module and try loading the font with a size of 75 or so.