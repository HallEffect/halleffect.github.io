Title: Сборка Boost.python с помощью MinGW
Date: 2015-05-13
Tags: Python, Boost
Category: Блог

1. Скачать [архив с сайта](http://www.boost.org/users/download/)
2. Распаковать в `C:\`
3. Перейти в папку `C:\boost_1_xx_x`
4. Выполнить:
```
    bootstrap.bat mingw
    b2 --build-type=complete --with-python stage
```
5. В папке `C:\boost_1_xx_x\stage\lib` будут лежать собранные `.dll`
>Расшифровка имен файлов приведена [здесь](http://www.boost.org/doc/libs/1_55_0/more/getting_started/windows.html#library-naming)

Для сборки x64 нужно использовать ключ `address-model=64`
```
b2 toolset=gcc --build-type=complete address-model=64 --with-python stage
```
>Сборку Boost.Python x64 нужно делать если установлен Python x64

Для сборки библиотеки с использованием C++11 используется ключевое слово `cxxflags="-std=c++11"`
```
b2 toolset=gcc cxxflags="-std=c++11" --build-type=complete  --with-python stage
```

Для ускорения сборки можно добавить ключ `-j n`, где `n` - число ядер на машине.

Если изменилась версия компилятора, библиотеку надо пересобирать

