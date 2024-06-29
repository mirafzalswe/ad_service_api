# Ad Service API

Ad Service API - это Django-проект, предназначенный для получения данных о первых 10 объявлениях с сайта Farpost. Проект предоставляет API для получения информации о конкретном объявлении по его ID.

## Технологии

- Python
- Django
- Django REST Framework
- Django REST Framework Authtoken

## Установка

### Клонирование репозитория

```bash
git clone https://github.com/yourusername/ad_service.git
cd ad_service
````
### Создание и активация виртуального окружения
```bash
pip install -r requirements.txt
```
### Применение миграций
```bash
python manage.py migrate
```
### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Запуск сервера
```bash
python manage.py runserver
```
## Использование

#### Аутентификация
Для доступа к защищенным эндпоинтам необходимо получить токен аутентификации.

#### Получение токена
Отправьте POST-запрос с именем пользователя и паролем на  `/api-token-auth/`:
```bash
curl -X POST -d "username=your_username&password=your_password" http://127.0.0.1:8000/api-token-auth/
```
#### Пример ответа
```json
{
    "token": "your_generated_token"
}
```
#### Эндпоинты
Создание нового пользователя (для всех)

```bash
POST /api/create_user/
```
#### Параметры запроса:
* `username`: Имя пользователя
* `password`: Пароль

#### Пример ответа 
```json 
{
    "usern_id": <user_id>,
    "username": <username>,
    "token" :  <token> 
}
```
#### Пример запроса:
```bash
curl -X POST -H "Authorization: Token your_admin_token" -d "username=new_user&password=new_password" http://127.0.0.1:8000/api/create_user/

```
#### Получение информации об объявлении по ID
```bash
GET /api/ads/<ad_id>/
```
#### Пример запроса:
```bash
curl -H "Authorization: Token your_token" http://127.0.0.1:8000/api/ads/1/
```
### Пример ответа
```json 
{
    "id": 1,
    "title": "Пример заголовка объявления",
    "ad_id": 12345,
    "author": "Автор объявления",
    "views": 100,
    "position": 1
}
```

## как запольнить таблицу ?
в гланом пакете adv_serv есть файл   `get_date.py`
#### набираем команде 
```bash
python manage.py shell
```
#### импортируем функию и запускаем
```bash
from adv_serv.get_date import get_from_file

get_from_file() 
```
данный заполняться в таблицу по указанному порядку 



