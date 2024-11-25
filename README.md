# selenium-jenkins
### версия драйвера chromedriver: 114.0.5735.90
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

# деплой

## вместо freestyle project в new item выбирайте pipeline project

в разделе advanced pipeline options нужно добавить нужный url репозитория и указать ветку test

в pipeline выбирайте pipeline script from scm, в выпадающем списке scm - git. далее заполнить форму с ссылкой на репозиторий(формата git clone), указать ветку test.