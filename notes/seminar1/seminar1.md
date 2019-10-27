## Заметки ##
1. Проекты с семинаров и для семинаров будут появляться в этом репозитории в соответсвующей ветке (предположительно, по ветке на семинар)

## Нужные команды ##

1. Создаем venv под проект (https://virtualenv.pypa.io/en/stable/userguide/):
```
virtualenv -p /usr/bin/python3.7 ~/envs/new_env
```
Параметр -p - путь до нужной версии python, второй параметр - место, куда положить файлы env-а (НЕ нужно размещать env в директории проекта и добавлять потом в гит)
2.Активируем env
```
source ~/envs/new_env/bin/activate
```

2. Устанавливаем django:
```
pip install django
```
Нужна версия 2.*

3. Создаем проект:
```
django-admin startproject <project_name>
```

4. Создаем файл со списком пакетов, которые использует проект:
```
pip freeze > requirements.txt
```
Если под проект создали отдельный venv, в файл попадут только нужные для проекта пакеты и их зависимости. Есть и другие способы генерировать такой файл автоматически (например, https://github.com/bndr/pipreqs)

5. Для установки пакетов для проекта, который использует файл requirements, достаточно написать
```
pip install -r requirements.txt
```
6. Создаем приложение внутри django-проекта
```
django-admin startapp <app_name>
```
7. Создаем миграции
```
python manage.py makemigrations
```
8. Применяем миграции
```
python manage.py migrate
```
9. Поднимаем dev-сервер (запускаем проект)
```
python manage.py runserver
```


## Материалы ##
1. project1_basics в данном репозитории - пример простого проекта с одним приложением tournaments и одной моделью Tournament (в коде есть совсем немного комментариев). Приложение позволяет создавать и редактировать турниры, получать их список
2. Части 1-4 туториала
https://docs.djangoproject.com/en/2.2/intro/tutorial01/
3. Про работу с формами - https://docs.djangoproject.com/en/2.2/topics/forms/ (в проекте есть одна простейшая форма)
4. ModelForms - формы на основе моделей - https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/
5. django templates: синтаксис -  https://docs.djangoproject.com/en/2.2/topics/templates/, переиспользование шаблонов - https://tutorial.djangogirls.org/en/template_extending/ Учитывая что в проекте фронт будет сделан на React, шаблоны особо не понадобятся, но могут быть удобны, например, если приложение будет отправлять пользователям письма - все виды писем можно будет отнаследовать от одного шаблона. В project1 все шаблоны переиспользуют base.html, заменяя блок body на свой собственный.
