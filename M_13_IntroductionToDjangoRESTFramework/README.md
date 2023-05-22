# DJANGO REST FRAMEWORK #

## Цель работы

Научиться применять Django REST framework для получения (в том числе фильтрации и поиска), создания, обновления, удаления сущностей в Django-приложении.

## Что сделано

1. Установлен и подключен `Rest Framework` 
   - Добавлен `rest_framework` в `INSTALlED_APPS`
   - Указан словарь `REST_FRAMEWORK`
   - Добавлены настройки пагинации 
2. Создан сериализатор для модлей:
   - Product
   - Order
3. Создан `ViewSet` для моделей:
   - Product
   - Order
4. Через `Default Router` подключены созданные `ViewSet` к `urls` в приложении `ShopApp`
5. Установлен и подключен `django-filter`:
   - Добавлен `django_filters` в `INSTALlED_APPS`    
   - Указан стандартный бэкэнд для фильрации `DEFAULT_FILTER_BACKENDS`
6. Добавьте правила фильтрации на `ViewSet` для `Product`
   - Правила поиска через `SearchFilter`
   - Правила сортировки через `OrderFilter`
7. Добавьте правила фильтрации на `ViewSet` для `Order`
   - Правила фильтрации через `DjangoFilterBackEend`
   - Правила сортировки через `OrderFilter`