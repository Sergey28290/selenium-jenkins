# selenium-jenkins
### версия драйвера chromedriver: 131.0.6778.85

# DEPLOY GUIDE

непосредственно в панели jenkins необходимо совершить действия:
1. New Item

1.1. выберите Freestyle project

2. перейдите в раздел Source code management

   
![image (1)](https://github.com/user-attachments/assets/59892b6c-4921-4aea-a974-4a192a3d18f4)


4. выберите Git, заполняем Repository URL, после этого примените изменения

   
![image-1](https://github.com/user-attachments/assets/11616d40-883a-4749-8a07-01eca0b08d32)


6. в разделе "Build" выберите "Add build step" и выберите "Execute Windows batch command". вставляете следующее:
```
python -m venv venv

call venv\Scripts\activate

pip install -r requirements.txt

set PATH=%PATH%;%cd%\chromedriver

pytest
```

если билд падает с ошибкой из-за того, что jenkins не знает команд pip, python, pytest - убедитесь, что у пользователя jenkins в path есть питон и его библиотеки.

решение:
1. переходите на дэшборд jenkins, клик на manage jenkins, далее system -> global properties (если не можете найти - используйте f3 для быстрого поиска по странице):

   
![image-3](https://github.com/user-attachments/assets/0cd5b9b4-e7e2-4f15-a4f6-71ff811f4d03)

## ОБРАТИТЕ ВНИМАНИЕ! список путей слитно через точку с запятой, типа `C:\Users\norma\AppData\Local\Programs\Python\Python312\;C:\Users\norma\AppData\Local\Programs\Python\Python312\Scripts\`


3. готово!
