Title: Перенаправление команды print в Python - посылка сигнала в PyQt
Date: 2016-02-20
Category: Блог
Tags: Python


В процессе работы, иногда, бывает необходимо сделать так, чтобы результат команды `print` помимо консоли был записан в файл.

Для этого можно перенаправить стандартный вывод в экземпляр пользовательского класса, у которого реализован метод `write(data(str))`

```python
class OutputBuffer(object):
    """
    Класс предназначен для перехвата потока вывода

    """

    def __init__(self, pathToLog):
        self.pathToLog = pathToLog

        # Сохраняем исходный поток вывода
        self.console = sys.stdout

    def write(self, text):
        """
        Напечатать результат в консоль и в файл

        Args:
            text(str) - данные для записи

        """
        f = open(self.pathToLog, "a")
        f.write(text)
        f.close()

        # Записать данные в буфер вывода
        self.console.write(text)

        # Вытолкнуть данные из буфера на консоль
        self.console.flush()

    def reset(self):
        """
        Вернуть исходный поток вывода

        """
        sys.stdout = self.console
```

Пример использования:
```python
# Перенаправляем стандартный вывод
sys.stdout = OutputBuffer("MySuperLogFile.txt")

# Этот текст будет напечатан и на консоль и в лог файл
print "Hello",
print "World"

# Только на консоль(вернули как было)
sys.stdout.reset()
print "Console only"
```

При разработки пользовательских графических приложений на PyQt возникают ситуации, когда необходимо выполнять некоторые функции в отдельном потоке, а стандартный вывод этих функций отображать в виджете. Для этого удобно использовать механизм сигналов и слотов. 
Для этого необходимо создать класс, унаследованный от `QObject`:
```python
class OutputBuffer(QObject):
    """
    Класс предназначен для перехвата потока вывода

    """

    def __init__(self):
        super(OutputBuffer, self).__init__()

        # Сохраняем исходный поток вывода
        self.console = sys.stdout

    def write(self, text):
        self.emit(SIGNAL("readyOutput"), text)
```

