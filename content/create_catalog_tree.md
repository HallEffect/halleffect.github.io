Title: Создание иерархического дерева каталогов
Date: 2016-03-31
Tags: Python
Category: Блог
slug: create_catalogue_tree

В процессе работы появилась задача отображения иерархического дерева каталогов относительно текущего пути.

Создаем класс для [перенаправления команды print](http://halleffect.github.io/articles/perenapravlenie-komandy-print-v-python-posylka-signala-v-pyqt/). Он будет использоваться для вывода с отступами, соответствующими уровням вложенности каталогов. Каждый уровень вложенности будет добавлять к выводу знак табуляции `\t`.
```python
import sys

class OutputBuffer(object):

    def __init__(self):
        self.console = sys.stdout
        self.indent = ""

    def write(self, text):
        self.console.write(self.indent + text)

    def addIndent(self):
        self.indent += "\t"

    def removeIndent(self):
        self.indent = self.indent[:-1]

```

Рекурсивная функция прохода по всем каталогам:
```python
import os

def printFiles(path):

    # Получаем список файлов и подкаталогов в каталоге path
    filesList = os.listdir(path)

    # Получаем список файлов в каталоге path
    files = [fileName for fileName in filesList if os.path.isfile(path + "/" + fileName)]

    # Получаем список подкаталогов в каталоге path
    subdirectories = [subdirectory for subdirectory in filesList if os.path.isdir(path + "/" + subdirectory)]

    # Проходим по всем подкаталогам в каталоге path
    for subdirectory in subdirectories:
        print subdirectory

        sys.stdout.addIndent()
        printFiles(path + "/" + subdirectory)
        sys.stdout.removeIndent()

        print

    for fileName in files:
        print fileName
```

Пример использования:
```python
# Перенаправляем стандартный вывод
sys.stdout = OutputBuffer()

printFiles(".")
```

Результат работы:
```
folder 1
    1.txt   
    2.txt   

folder 2
    folder 1    
        folder 1        
        
        folder 3        
            1.txt           
            2.txt           
        
        folder 4        
        
        folder 5        
        
        1.txt       
        2.txt       
    
    folder 3    
    
    folder 4    
    
    folder 5    
        1.txt       
        2.txt       
    
    1.txt   
    2.txt   

folder 3

folder 4

folder 5

1.txt
2.txt
```
