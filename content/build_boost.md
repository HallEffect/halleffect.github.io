Title: Сборка Boost.python с помощью MinGW
Date: 2015-05-13
Tags: Python, Boost
Category: Блог

- Скачать [архив с сайта](http://www.boost.org/users/download/)
- Распаковать в `C:\`
- Перейти в папку `C:\boost_1_xx_x`
- Выполнить:
```
bootstrap.bat mingw
b2 toolset=gcc --build-type=complete --with-python stage
```
- В папке `C:\boost_1_xx_x\stage\lib` будут лежать собранные `.dll`
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

Если при сборке Boost.python на компьютере установлен `Python 2.7.10 x32` (на x64 не проверялось), то могут появиться следующие ошибки:
```
C:\Python27\libs/libpython27.a(dmmes01026.o):(.idata$7+0x0): undefined reference to `_head_C__build27_cpython_PCBuild_libpython27_a'
C:\Python27\libs/libpython27.a(dmmes00220.o):(.idata$7+0x0): undefined reference to `_head_C__build27_cpython_PCBuild_libpython27_a'
C:\Python27\libs/libpython27.a(dmmes00363.o):(.idata$7+0x0): undefined reference to `_head_C__build27_cpython_PCBuild_libpython27_a'
C:\Python27\libs/libpython27.a(dmmes00386.o):(.idata$7+0x0): undefined reference to `_head_C__build27_cpython_PCBuild_libpython27_a'
C:\Python27\libs/libpython27.a(dmmes00136.o):(.idata$7+0x0): undefined reference to `_head_C__build27_cpython_PCBuild_libpython27_a'
C:\Python27\libs/libpython27.a(dmmes00705.o):(.idata$7+0x0): more undefined references to `_head_C__build27_cpython_PCBuild_libpython27_a' follow 

collect2.exe: error: ld returned 1 exit status
```
Проблема в файле `C:\Python27\libs\libpython27.a`. Файл можно взять из предыдущей версии `Python 2.7.9` или обновиться до `2.7.11`