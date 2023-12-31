# Загрузка и обработка файлов

## Описание ТЗ

Перед получением информации о выполненном проекте предлагаю ознакомиться с подробной информацией о целях проета:

<details>
  <summary>Открыть</summary>

### Требования:

1. Создать Django проект и приложение.
2. Использовать Django REST Framework для создания API.
3. Реализовать модель File, которая будет представлять загруженные файлы. Модель должна содержать поля:
   - file: поле типа FileField, используемое для загрузки файла.
   - uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.
   - processed: поле типа BooleanField, указывающее, был ли файл обработан.
4. Реализовать сериализатор для модели File. 
5. Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели File, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.

6. Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.
7. Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.

### Дополнительные требования:

1. Использовать Docker для развертывания проекта.
2. Реализовать механизм для обработки различных типов файлов (например, изображений, текстовых файлов и т.д.).
3. Предусмотреть обработку ошибок и возвращение соответствующих кодов статуса и сообщений об ошибках.

### Примечания:

- При выполнении задания рекомендуется использовать официальную документацию Django, DRF, Celery и Docker.
- Вы можете использовать любые дополнительные библиотеки, если считаете нужным.

### Усложения:

- Тесты (постарайтесь достичь покрытия в 70% и больше)
- Опишите, как изменится архитектура, если мы ожидаем большую нагрузку
- Попробуйте оценить, какую нагрузку в RPS сможет выдержать ваш сервис

</details>

## О выполненном проекте filemanager

Этот проект представляет собой API для загрузки, обработки и управления файлами различных форматов, включая .txt и .pdf для текстовых файлов и изображения для изображений. Проект разработан с использованием Django и Django REST Framework и предоставляет возможность загружать файлы, а затем асинхронно обрабатывать их. В случае текстовых файлов .txt и .pdf происходит сохранение содержимого в базу данных, а для изображений выполняется форматирование и обработка. 

### Важными особенностями проекта являются:

- **Контейнеризация с Docker**: Проект упакован в контейнеры с использованием Docker и Docker Compose, обеспечивая легкость развертывания в различных окружениях.

- **Масштабируемость с Celery**: Для обработки файлов реализована асинхронная обработка с помощью Celery, что делает приложение более отзывчивым и способным обрабатывать большие объемы данных.

- **Юнит-тестирование**: Для обеспечения стабильности и надежности приложения разработан набор юнит-тестов, проверяющих работу ключевых компонентов, включая URL-адреса и обработчики ошибок. Эти тесты обеспечивают надежную работу приложения.

Документацию к API можно найти в Swagger и Redoc, что позволяет легко понимать и использовать его функциональность.

### Используемый стек

- **Python**: Версия 3.9.
- **Django**: Версия 3.2.
- **Django REST framework**: Библиотека для разработки RESTful API.
- **python-dotenv**: Загрузка переменных окружения из файлов .env для конфигурации.
- **Celery**: Асинхронная обработка файлов в фоновом режиме.
- **psycopg2-binary**: Адаптер для работы с базой данных PostgreSQL.
- **redis**: Сервер для хранения задач в Celery и асинхронной обработки.
- **Pillow**: Библиотека для работы с изображениями.
- **PyMuPDF**: Извлечение текста из PDF-файлов.
- **drf-spectacular**: Создание интерактивной документации для API.
- **gunicorn**: WSGI HTTP-сервер для обслуживания Django-приложения.
- **pre-commit**: Автоматическая проверка и форматирование кода перед коммитом (blake8)


### Внешнее ПО

- **PyCharm**: Интегрированная среда разработки Python.
- **Docker**: Контейнеризация приложения и зависимостей для легкого развертывания.
- **Postman**: Инструмент для тестирования и проверки функциональности API.
- **Google Chrome**: Браузер для проверки работоспособности приложения.

## Демонстрация приложения на активном сервере
(СЕЙЧАС ВЫКЛЮЧЕН, СМОТРИТЕ ЛОКАЛЬНЫЙ ВАРИАНТ)

### Доступные пути API

- **http://62.84.127.157/api/v1/files/**: список загруженных файлов с их данными, включая текущий статус обработки.
- **http://62.84.127.157/api/v1/upload/**: путь для принятия POST-запросов на загрузку файлов
- **http://62.84.127.157/api/v1/files/<id>/**: информация о конкретном загруженном файле (id необходимо поменять на конкретный файл, id скрыты от пользователей, но доступны в админ-консоли)


- **http://62.84.127.157/api/v1/redoc/**: Redoc - Интерактивная документация API для ознакомления с функциональностью и использованием.
- **http://62.84.127.157/api/v1/swagger-ui/#/**: Swagger - Интерактивная документация API с возможностью отправки запросов и получения ответов непосредственно из браузера для тестирования.

### Админ-консоль

http://62.84.127.157/admin/ - админ-консоль
```shell
Параметры входа:
    Username = admin
    Passowrd = test_admin
 ```
http://62.84.127.157/admin/files/file/ - список загруженных файлов
http://62.84.127.157/admin/files/textdocument/ - список обработанных текстовых файлов


## Локальный запуск приложения

Для локальной установки проекта необходимо выполнить следующие шаги:

### Установка и настройка внешнего ПО:
- Docker: Если у вас ещё не установлен Docker, следуйте инструкциям на официальном сайте Docker для вашей операционной системы: https://docs.docker.com/get-docker/. После установки убедитесь, что Docker Daemon запущен. 
- Docker Compose: Установите Docker Compose, если он ещё не установлен. Docker Compose используется для управления многоконтейнерными приложениями. Инструкции по установке можно найти здесь: https://docs.docker.com/compose/install/

### Запуск приложения:
- Клонирование репозитория
```shell
git clone git@github.com:Leenominai/test_picasso.git
```
- Переход в каталог репозитория
```shell
cd test_picasso
cd backend
```
- Настройка файлов окружения: Создайте файл окружения .env в корне вашего проекта.
- Скопируйте все данные из файла .env.example в файл .env
  - Сейчас в файле .env.example присутствуют значения всех необходимых переменных только для локальной проверки приложения, а для сервера все переменные скрыты в GitHub Secrets.
- Запуск контейнеров: Запустите приложение с помощью Docker Compose:
```shell
cd ..
cd docker_local
docker-compose up -d
```
- Применение миграций: Примените миграции Django для создания необходимых таблиц в базе данных:
```shell
docker exec -it test_backend bash
python manage.py migrate
exit
```
- Создание профиля суперпользователя для доступа в админ-консоль (по желанию):
```shell
docker exec -it test_backend bash 
python manage.py createsuperuser
exit
```

- Проверочное тестирования внутри проекта (по желанию)

Уделено внимание тестированию нашего приложения. Это важно для обеспечения стабильности и надежности приложения. На сервере оно выполняется автоматически, а на локальной машине это можно проверить в ручную:
```shell
docker exec -it test_backend bash
python manage.py test -v 2
exit
```
- Открытие приложения:
Ваше приложение должно быть доступно по адресу http://127.0.0.1:8000/ в браузере.


### Доступные пути API

- **http://127.0.0.1:8000/api/v1/files/**: список загруженных файлов с их данными, включая текущий статус обработки.
- **http://127.0.0.1:8000/api/v1/upload/**: путь для принятия POST-запросов на загрузку файлов
- **http://127.0.0.1:8000/api/v1/files/<id>/**: информация о конкретном загруженном файле (id необходимо поменять на конкретный файл, id скрыты от пользователей, но доступны в админ-консоли)


- **http://127.0.0.1:8000/api/v1/redoc/**: Redoc - Интерактивная документация API для ознакомления с функциональностью и использованием.
- **http://127.0.0.1:8000/api/v1/swagger-ui/#/**: Swagger - Интерактивная документация API с возможностью отправки запросов и получения ответов непосредственно из браузера для тестирования.

### Админ-консоль

- **http://127.0.0.1:8000/admin/**: админ-консоль
```shell
    Параметры входа те, которые вы прописывали при создании профиля администратора.
 ```
- **http://127.0.0.1:8000/admin/files/file/**: список загруженных файлов
- **http://127.0.0.1:8000/admin/files/textdocument/**: список обработанных текстовых файлов

## Тестирование в Postman

Для тестирования через программу Postman необходимо:
- Установить её на свою рабочую машину с официального сайта: https://www.postman.com/
- После установки необходимо перейти в раздел Workspaces
- Создать новый Request через +, либо изменить стандартный
- В шкалу URL необходимо ввести следующий адрес:
  - При работе через сервер: http://62.84.127.157/api/v1/upload/
  - При работе через локальную машину: http://127.0.0.1:8000/api/v1/upload/
- Слева от введённого адреса выбрать тип запроса: POST
- Далее, необходимо выбрать блок Body и раздел form-data под ним.
- Для загрузки используем следующий формат:
```shell
    Key = file (так же сбоку выбираем тип - file)
    Value = (загружаем файл для загрузки)
```
Для загрузки файлов существуют следующие разрешения:
- Доступные типы файлов для загрузки: тип image, а так же файлы формата .pdf, .txt
- Для загрузки достпен множественный выбор файлов разных типов.
- Можно загружать разные типы файлов одновременно.

При возможных ошибках загрузок в блоке Headers ставим следующую настройку:
```shell
    Key = ContentType
    Value = multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
```
    
Ответ системы будет в виде:
```shell
[
    {
        "file": "/uploads/345_HWoRWbk.png",
        "uploaded_at": "2023-09-23T10:33:02.856669Z",
        "processed": false
    }
]
```
- "processed": false - это значение указывает, что файл еще не был полностью обработан в момент ответа на запрос о загрузке. Наше приложение использует асинхронный процесс обработки файлов с помощью Celery, поэтому файлы могут быть обработаны после загрузки. Вы можете проверить статус обработки файла, используя соответствующий путь API или админ-консоль.

## Разработчики

Проект разработан и поддерживается Александром Рассыхаевым.

GitHub: [Ссылка на GitHub профиль](https://github.com/Leenominai)

Telegram: [@Leenominai](https://t.me/Leenominai)
