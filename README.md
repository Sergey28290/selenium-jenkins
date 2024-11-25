# selenium-jenkins
### версия драйвера chromedriver: 114.0.5735.90
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

# деплой

## нужные плагины: 
- Pipeline: Utility Steps
- JUnit Plugin
- Allure Jenkins Plugin
- Email Extension Plugin
- Pipeline: Groovy Plugin

## методы, которые нужно разрешить:
```
method hudson.model.Actionable getAction java.lang.Class
method hudson.tasks.test.AbstractTestResultAction getFailCount
method hudson.tasks.test.AbstractTestResultAction getFailedTests
method hudson.tasks.test.AbstractTestResultAction getSkipCount
method hudson.tasks.test.AbstractTestResultAction getTotalCount
method net.sf.json.JSONArray join java.lang.String
method org.jenkinsci.plugins.workflow.support.steps.build.RunWrapper getRawBuild
```

## вместо freestyle project в new item выбирайте pipeline project

в разделе advanced pipeline options нужно добавить нужный url репозитория и указать ветку test

в pipeline выбирайте pipeline script from scm, в выпадающем списке scm - git. далее заполнить форму с ссылкой на репозиторий(формата git clone), указать ветку test.

![image](https://github.com/user-attachments/assets/2733654a-1ce7-4a46-831d-a16b7bcfb810)


# важный момент - в additional behaviours выберите clean before checkout

![image](https://github.com/user-attachments/assets/ffab2c64-e591-444a-ad93-a34d7a2185e0)


также необходимо настроить smtp сервер.

сначала нужно добавить credentials для smtp: Manage Jenkins -> Credentials

![image](https://github.com/user-attachments/assets/264bd480-7411-462b-b8bc-95e995353b31)


данные(логин, пароль) берем с smtp сервиса, который предоставил доступы. ветка под gmail smtp.

хороший туториал для настройки и проверки gmail smtp: https://www.youtube.com/watch?v=ZfEK3WP73eY

для работы пайплайна нужно будет скачать gdrive, создать проект в google cloud console и авторизоваться, это достаточно просто и занимает пару минут: https://github.com/glotlabs/gdrive. документация: https://github.com/glotlabs/gdrive/blob/main/docs/create_google_api_credentials.md

## обратите внимание, чтобы пользователю jenkins была доступна конфигурация gdrive. специально добавлена проверка в шаге загрузки на драйв - gdrive acconut list, если список пуст и билд падает - значит пользователь jenkins не видит конфиг gdrive. проблему можно исправить сменой пользователя jenkins/добавлением аккаунта gdrive от имени пользователя jenkins через powershell

как только привязали все в gdrive - зайдите в google drive, создайте папку, ПКМ, затем share, доступ anyone with the link, из ссылки взять идентификатор папки и вставить в jenkinsfile(https://drive.google.com/drive/folders/YOUR_FOLDER_ID?usp=sharing) 


далее Manage Jenkins -> Configure System, раздел Extended E-mail Notification.

заполнять все поля как в credentials, под вводом порта нажать advanced, там выбрать созданный объект credentials.

получателей можно настроить в recipients.html

# траблшутинг
## если все сделано правильно, а билд падает с ошибкой - прочитайте лог и сделайте вывод, установлены ли нужные плагины или jenkins требует разрешить метод из jenkinsfile. также может возникать ошибка permission denied, если вы запустили allure, но забыли убить batch и у jenkins нет прав на удаление папки с репортом во время очистки воркспейса из-за этого
