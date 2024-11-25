# selenium-jenkins
### версия драйвера chromedriver: 114.0.5735.90
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

# деплой

## вместо freestyle project в new item выбирайте pipeline project

в разделе advanced pipeline options нужно добавить нужный url репозитория и указать ветку test

в pipeline выбирайте pipeline script from scm, в выпадающем списке scm - git. далее заполнить форму с ссылкой на репозиторий(формата git clone), указать ветку test.

также необходимо разрешить методы и настроить smtp сервер.

сначала нужно добавить credentials для smtp: Manage Jenkins -> Credentials

![alt text](image.png)

данные(логин, пароль) берем с smtp сервиса, который предоставил доступы. можно использовать brevo, mailtrap ... от себя порекомендую использовать gmail smtp, быстро и просто. не все smtp сервисы дают нормально зарегистрироваться - можно сразу после регистрации по неизвестным причинам влететь под suspend

хороший туториал для настройки и проверки gmail smtp: https://www.youtube.com/watch?v=ZfEK3WP73eY

далее Manage Jenkins -> Configure System, раздел Extended E-mail Notification.

заполнять все поля как в credentials, под вводом порта нажать advanced, там выбрать созданный объект credentials.

отправку писем от jenkins также можно проверить в разделе ниже - email notification. заполнить все поля и нажать чекбокс Test configuration by sending test e-mail