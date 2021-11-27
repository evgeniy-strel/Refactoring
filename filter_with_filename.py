from PIL import Image
import numpy as np
import time;

class Mozabrick:
    def __init__(self, pixels, size, count_gray):
        """Инициализация всех переменных
        pixels - все пиксели картинки в трех-мерном массиве(таблица пикселей и их RGB)
        height - кол-во пикселей по высоте
        width - кол-во пикселей по ширине
        size - размер мозайки
        count_gray - количество степеней серого цвета
        """
        self.pixels = pixels;
        self.height = len(pixels);
        self.width = len(pixels[1]);
        self.size = size;
        self.count_gray = count_gray;
    def image_processing(self):
        """Обработка изображения, в которой мы проходимся по всем пикселям
        с шагом равным размеру мозайки. Для каждого пикселя высчитваем среднюю яркость
        и окрашиваем пиксели мозайки в это значение. Возвращается измененное изображение.
        """
        for i in range(0, self.height, self.size):
            for j in range(0, self.width, self.size):
                medium_brightness = self.get_medium_brightness(i, j);
                self.color_pixels(i, j, medium_brightness);
        return Image.fromarray(self.pixels);
    def color_pixels(self, i, j, medium_brightness):
        """Функция матрично окрашивает нужный пиксель и соседние мозаичные 
        в заданное значение средней яркости"""
        self.pixels[i : i + self.size, j : j + self.size] = medium_brightness // self.count_gray * self.count_gray // 3;
    def get_medium_brightness(self, i, j):
        """Функция возвращает среднюю яркость пикселя и соседних мозаичных 
        путем сложения трех каналов цветов RGB и деления на количество пикселей"""
        sumRgb = self.pixels[i : i + self.size, j : j + self.size].sum();
        return int(sumRgb // (self.size ** 2));

startTime = time.time();
inputImg = Image.open('img2.jpg');
outputNameImg = 'output.jpg';
size = 10;
count_gray = 50;
pixels = np.array(inputImg);
mozabrick = Mozabrick(pixels, size, count_gray);
result = mozabrick.image_processing();
result.save(outputNameImg); 
endTime = time.time();
print();
print(f'Время выполнения программы составило: {endTime - startTime} секунд');