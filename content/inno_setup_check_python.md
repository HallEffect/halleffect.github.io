Title: Полезности по работе с Inno Setup
Date: 2016-02-21
Tags: Inno setup
Category: Блог
slug: inno_setup_howto

###Запуск .msi инсталлятора после установки:
```html
[Files]
Source: "Your-MSI-File.msi"; DestDir: "{tmp}"

[Run]
Filename: "msiexec.exe"; Parameters: "/i ""{tmp}\Your-MSI-File.msi"""
```

###Изменение баннера слева и картинки в правом верхнем углу инсталлятора:
```
WizardImageFile=logo_big.bmp
WizardSmallImageFile=logo.bmp
```
Требовая к картинкам:

- Размер баннера: 164x314 px, 256 цветов
- Размер картинки: 55x58 px, 256 цветов

###Проверка установки Python и получение его каталога установки:
```pascal
[Code]
function GetDefRoot(Param: String): String;

var path:String;

begin
    // Проверяем путь установки Python для x64 машины
    if RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Wow6432Node\Python\PythonCore\2.7\InstallPath', '',path) then
    begin
        Result := path;
    end
    else
    begin
        // Проверяем путь установки Python для x32 машины
        if RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Python\PythonCore\2.7\InstallPath', '',path) then
        begin
            Result := path;
        end
        else
        begin
            MsgBox('Python 2.7 не найден на данном компьютере. Сначала установите Python 2.7', mbInformation, MB_OK);
            abort();
        end
    end
end;
```

Можно использовать, например, так:
```
DefaultDirName={code:GetDefRoot}\Lib\site-packages\my_packet
```
