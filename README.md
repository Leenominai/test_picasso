# File Upload and Processing API

Этот проект представляет собой Django-приложение, реализующее API для загрузки и обработки файлов. Проект использует Django REST Framework и Celery для создания API и асинхронной обработки файлов.

## Доступ через сервер

### Доступные пути API

```shell
http://127.0.0.1:8000/api/v1/files/ - список загруженных файлов с их данными, включая текущий статус обработки.
http://127.0.0.1:8000/api/v1/files/<id>/ - информация о конкретном загруженном файле
http://127.0.0.1:8000/api/v1/upload/ - путь для принятия POST-запросов
```

### Админ-консоль

```shell
http://62.84.127.157/admin/ - админ-консоль
    Параметры входа:
        Username = admin
        Passowrd = test_admin
http://62.84.127.157/admin/files/file/ - список загруженных файлов
http://62.84.127.157/admin/files/textdocument/ - список обработанных текстовых файлов
```

### Тестирование в Postman

```shell
Вводим следующий адрес и выбираем POST-запрос:
http://62.84.127.157/api/v1/upload/
Выбираем блок Body и раздел form-data.
Для загрузки используем следующий формат:
    Key = file (так же сбоку выбираем тип - file)
    Value = (загружаем файл для загрузки)
Отмечаем галочками необходимое количество файлов и загружаем
```

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

"processed": false - потому что файл ещё не успел быть обработан системой, 
но при проверке файла он уже будет обработан.
```

## Локальный запуск

Для локальной установки проекта выполните следующие шаги:

```shell
git clone git@github.com:Leenominai/test_picasso.git
cd docker_local
docker-compose up -d
docker exec -it itm_backend bash
python manage.py migrate
# Теперь необходимо создать аккаунт суперпользователя для входа в админ-консоль:
python manage.py createsuperuser
exit
```
