# Проект opening-hours

## Описание проекта:

Проект **opening-hours** имеет endpoint `/opening_hours`, который принимает массив входных данных в формате JSON с часами работы ресторана. 

Входной JSON состоит из ключей, указывающих дни недели и соответствующие часы работы в качестве значений. Один файл JSON содержит данные для одного ресторана.
```
{
  <dayofweek>: <opening hours>
  <dayofweek>: <opening hours>
  ...
}
```
dayofweek: monday / tuesday / wednesday / thursday / friday / saturday / sunday

opening hours: массив объектов, содержащих часы работы. Каждый объект состоит из двух ключей:
-	type: open or close
-	value: время открытия / закрытия как время UNIX. Например: 32400 = 9 AM, 37800 = 10:30 AM

В качестве ответа к запросу возвращается человекочитаемый формат. Например: Saturday: 9 AM -11 AM, 4 PM - 11 PM

### Документация проекта:

После запуска сервиса докуменация доступна по адресам `/docs` и `/redoc`

## Технологии проекта:

- Python 3.9
- FastAPI 0.78.0
- Pydantic 1.10.13
- Uvicorn 0.17.6

## Установка:

Для установки проекта на локальной машине необходимо:

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:alekseikoznov/opening-hours.git
```
```
cd opening-hours
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас Windows
    ```
    source venv/scripts/activate
    ```
3. Обновить менеджер пакетов pip:
```
python -m pip install --upgrade pip
```
4. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
5. Запустить приложение:
```
uvicorn app.main:app
```
6. После успешного запуска проект станет доступен по адресу: http://127.0.0.1:8000/


## Примеры запросов к API:

#### Отправка массива с данными закрытия и открытия: POST http://127.0.0.1:8000/opening_hours
```
{
  "monday": [],
  "tuesday": [
   {
      "type": "open",
      "value": 36000
   },
   {
    "type": "close",
    "value": 64800
   }
  ],
  "wednesday": [],
  "thursday": [
   {
    "type": "open",
    "value": 37800
   },
   {
    "type": "close",
    "value": 64800
   }
  ],
  "friday": [
   {
    "type": "open",
    "value": 36000
   }
  ],
  "saturday": [
   {
    "type": "close",
    "value": 3600
   },
   {
    "type": "open",
    "value": 36000
   }
  ],
  "sunday": [
   {
    "type": "close",
    "value": 3600
   },
   {
    "type": "open",
    "value": 43200
   },
   {
    "type": "close",
    "value": 75600
   }
  ]
}
```
#### Пример ответа:
```
{
  "Monday": "Closed",
  "Tuesday": "10 AM - 6 PM",
  "Wednesday": "Closed",
  "Thursday": "10:30 AM - 6 PM",
  "Friday": "10 AM - 1 AM",
  "Saturday": "10 AM - 1 AM",
  "Sunday": "12 PM - 9 PM"
}
```
