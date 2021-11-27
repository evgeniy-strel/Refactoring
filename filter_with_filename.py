from PIL import Image
import numpy as np
import time;

class Mozabrick:
    def __init__(self, pixels, size, count_gray):
        self.pixels = pixels;
        self.height = len(pixels);
        self.width = len(pixels[1]);
        self.size = size;
        self.count_gray = count_gray;
    def image_processing(self):
        for i in range(0, self.height, self.size):
            for j in range(0, self.width, self.size):
                medium_brightness = self.get_medium_brightness(i, j);
                self.color_pixels(i, j, medium_brightness);
        return Image.fromarray(self.pixels);
    def color_pixels(self, i, j, medium_brightness):
        self.pixels[i : i + self.size, j : j + self.size] = medium_brightness // self.count_gray * self.count_gray // 3;
    def get_medium_brightness(self, i, j):
        sumRgb = self.pixels[i : i + self.size, j : j + self.size].sum();
        return int(sumRgb // (self.size ** 2));

startTime = time.time();
inputImg = Image.open('img2.jpg');
outputNameImg = 'output.jpg';
size = 10;
count_gray = 50;
pixels = np.array(inputImg);
result = Mozabrick(pixels, size, count_gray).image_processing();
result.save(outputNameImg); 
endTime = time.time();
print();
print(f'Время выполнения программы составило: {endTime - startTime} секунд');