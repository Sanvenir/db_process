pyuic5 -o ui_mainwindow.py mainwindow.ui
pyinstaller -y --clean -p D:\Users\sanve\AppData\Local\Programs\Python\Python35\Lib\site-packages\PyQt5\Qt\bin\Qt5WebChannel.dll main.py