## Описание проекта

Проект по автоматизации тестирования cms Opencart.


+ В директории tests/ находятся файлы с тестами для отдельных страниц.
  
  - tests/test_register.py - тесты на регистрацию
  - tests/test_admin_panel.py - тесты на страницу Административной панели
  - tests/test_catalog.py - тесты на страницу Каталога
  - !tests/test_header_page.py - тесты на Шапку сайта
  - tests/test_login_page.py - тесты на страницу Авторизации пользователя
  - tests/test_main_page.py - тесты на Главную страницу
  - tests/test_product.py - тесты на страницу Товара
  - !tests/test_search_page.py - тесты на страницу поиска
  - tests/test_product_card.py - тесты на корзину
____

## Список необходимых предустановленных приложений и утилит

- Python3 - для локального и удаленного (selenoid) запуска через консоль/ide
- Chromedriver - для локального запуска тестов в Chrome
- Geckodriver - для локального запуска тестов в Firefox
- Docker - для запуска тестов в контейнере и в Jenkins + для запуска opencart
- Selenoid + образы нужных браузеров - для удаленного запуска через консоль/ide/docker/jenkins
- Allure - для получения отчета при запуске через консоль/ide/docker
- Jenkins - для запуска в Jenkins
____

## Запуск приложения Opencart
(Должен быть всегда запущен для прогона тестов)

1. Запустить Docker
2. Приложение собирается из docker-compose.yml
Значение для OPENCART_HOST передается в командной строке через переменную local_ip - адрес вашей машины в сети
(узнать через ifconfig).
Выполнить команду:

```
local_ip={OPENCART_HOST} docker-compose up -d
```
После этого станут доступны: 
- приложение local_ip:80,
- админка local_i:8888,
- БД local_i:3306.
______

## Установка для локального и удаленного запуска тестов через ide/консоль
Установить - Python3, Chromedriver, Geckodriver, Allure, Selenoid (+образы браузеров)


### Общие шаги
- Скачать репозиторий на свою машину:

```
git clone repository_url
```

- Перейти в директорию скачанного репозитория

- Установить и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```
- Обновить PIP и установить зависимости:

```
pip install -U pip
pip install -r requirements.txt
```

- Выбрать интерпретатор для проекта (для запуска тестов через консоль/ide)

- Запустить Opencart

- После запуска тестов одним из вариантов представленных ниже получить Allure отчет:
В консоли выполнить команду, в качестве параметра указав путь до исполняемого файла allure на вашей машине:

```
./run_allure_report.sh /path/to/allure/bin
Пример: ./run_allure_report.sh /Applications/allure/bin/allure
```


#### Локальный запуск

В консоли (из директории проекта) выполнить команду:

```
pytest --local  --url=your_external_ip --browser-name=(firefox/chrome)  --executor=path_to_driver -n 2 --bv=browser_version
```
где:

- -n - во сколько потоков запускать тесты, если не указывать параметр при запуске - тесты будут запущены в 1 поток.

- --local - запускает тесты локально

- --url - адрес машины в сети (где запущен opencart)

- --browser-name - какой браузер запускать

- --executor - путь до драйвера на машине 
  
- --bv - версия браузера



#### Удаленный запуск (Selenoid)

1.Запустить Selenoid:
перейти в директорию с исполняемым файлом и выполнить команды, указав вместо ./bin имя исполняемого файла:
UI станет доступен на localhost:8080.
```
./bin selenoid start
./bin selenoid-ui start
```

2.В консоли (из директории проекта) выполнить команду:

```
pytest  --url=your_external_ip --browser-name=(chrome/firefox/opera) --browser-version --executor=selenoid_host -n 2
```
где:

- -n - во сколько потоков запускать тесты, если не указывать параметр при запуске - тесты будут запущены в 1 поток.

- --url - адрес машины в сети (где запущен opencart)

- --browser-name - какой браузер запускать

- --browser-version - версия указанного браузера

- --executor - хост selenoid-а (если на своей машине - 127.0.0.1)
____



## Запуск тестов в Docker + Selenoid
Установить - Docker, Allure, Selenoid (+образы браузеров)

- Скачать репозиторий на свою машину:

```
git clone repository_url
```

- Перейти в директорию скачанного репозитория


- Запустить Docker + приложение opencart

- Запустить тесты и получить отчет командой в консоли, в качестве параметров указав 
адрес машины в сети (где запущен opencart), 
браузер, версия браузера, хост selenoid-а (внешний)
и путь до исполняемого файла allure на вашей машине:

```
./run_test_in_docker_with_allure.sh your_external_ip browser browser_version selenoid_host(external) /path/to/allure/bin

Пример: ./run_test_in_docker_with_allure.sh 123.123.123.123 chrome 87.0 123.123.123.123 /Applications/allure/bin/allure
```

## Запуск тестов в Jenkins + Docker + Selenoid
Установить - Docker, Selenoid (+образы браузеров), Jenkins, плагин Allure для Jenkins

- Запустить Docker + приложение Opencart

- Запустить Selenoid (Jenkins в нем будет запускать тесты)

- Запустить Jenkins

- В Jenkins создать PipeLine

- Добавить в сборку параметры:
  + URL - хост с opencart
  + BROWSER_NAME  - в каком браузере запускать
  + BROWSER_VERSION - в какой версии браузера запускать
  + EXECUTOR - хост selenoid-а
  + NODES - значение по-умолчанию 1 (количество потоков)
  + DOCKER_PATH - путь до исполняемого файла Docker на машине
  
- Выбрать Pipeline script from SCM

- Выбрать SCM - Git

- Указать ссылку на репозиторий на Github

- Проверить название ветки - */main

- Сохранить пайплайн

- Собрать с необходимыми параметрами 
____
