import os ##модуль функций для работы  с операционкой

def finder(): ## пишем функцию поиска файлов chi
    place = os.getcwd() #смотрим куда закинули файл py, присваеваем путь переменной place
    for file in os.listdir(place): ##бегаем по всем файлам, listdir это список всех файлов по адресу в place
        if file.endswith(".chi"): ##берем все с расширением .chi
            file_chi = os.path.join(place, file) ##пишем в переменную file_chi путь до файла.chi
            name = os.path.splitext(file_chi)[0] ## записываем в name имя файла без расширения
            ## прочитаем файл построчно
            with open(file_chi, 'r') as f:
                lines = f.readlines()
            ## берем имя файла без расширения добавляем к нему NH.chi и записываем начиная с 4й строки
            with open(name+"NH.chi", 'w') as f:
                f.writelines(lines[4:])

## запускаем функцию finder()
if __name__ == '__main__':
    finder()