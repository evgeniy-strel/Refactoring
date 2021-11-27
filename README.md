# Refactoring
Время выполнения измерялось через модуль time путем разницы переменных end = time.time, расположенной в конце программы, и start = time.time перед ее началом.

Время выполнения начального файла old_filter.py
![Image alt](https://github.com/evgeniy-strel/Refactoring/blob/main/old_filter.jpg?raw=true)

Время выполнения окончательного файла filter.py
![Image alt](https://github.com/evgeniy-strel/Refactoring/blob/main/filter.jpg?raw=true)
Увеличение времени работы программы объясняется тем, что большая часть времени уходит на ввод данных пользователем: название картинок, размеров мозайки и степеней серого.

Время выполнения окончательного файла filter_with_filename.py
![Image alt](https://github.com/evgeniy-strel/Refactoring/blob/main/filter_with_filename.jpg?raw=true)
Сокращение времени в сравнении с файлом old_filter.py объясняется отказами от использования многочисленных циклов и их заменой матричными методами.

Скриншот вызова docstring описания функций:
![Image alt](https://github.com/evgeniy-strel/Refactoring/blob/main/doctest.jpg?raw=true)

Вывод на экран свойств ширины и высоты изображения, его формата, ширины блока и количество градаций серого:
![Image alt](https://github.com/evgeniy-strel/Refactoring/blob/main/values.jpg?raw=true)
