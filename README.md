# selenium-jenkins
### версия драйвера chromedriver: 114.0.5735.90
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

# деплой

## вместо freestyle project в new item выбирайте pipeline project

в разделе advanced pipeline options нужно добавить нужный url репозитория и указать ветку test

в pipeline выбирайте pipeline script from scm, в выпадающем списке scm - git. далее заполнить форму с ссылкой на репозиторий(формата git clone), указать ветку test.

также необходимо разрешить методы и настроить smtp сервер.

Manage Jenkins -> Configure System, раздел Extended E-mail Notification.

в поле "SMTP server" введите адрес вашего SMTP-сервера (что-то вроде smtp.gmail.com)
в поле "Default user e-mail suffix введите домен вашей электронной почты (@example.com).
в поле "SMTP Authentication" выберите "Use SMTP Authentication".
в поле "User Name" введите имя пользователя SMTP-сервера
в поле "Password" введите пароль для вашего SMTP-сервера.
в поле "Use SSL" установите флажок, если нужен ssl.
в поле "SMTP Port" введите порт вашего SMTP-сервера