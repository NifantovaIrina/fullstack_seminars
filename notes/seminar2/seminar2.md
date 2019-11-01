## Связи между моделями ##
### OneToOne
https://docs.djangoproject.com/en/2.2/topics/db/examples/one_to_one/
### ManyToOne
https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_one/
### ManyToMany
https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/

Если у одной модели Model1 есть отношение ForeignKey или ManyToMany на Model2, то из инстанса Model2 можно получить связанные объекты типа Model1 с помощью RelatedManager https://docs.djangoproject.com/en/2.2/ref/models/relations/

## Админка django ##
https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

Чтобы сделать модель видимой из админского интерфейса, нужно написать
```
admin.site.register(ModelName)
```
в файле admin.py приложения, содержащего эту модель.
## REST framework ##
### Принцип REST ###
### CORS headers ###
от чего защищаемся
как защищаемся
ставим
