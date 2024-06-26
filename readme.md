## Installation
1. Run ```pip install -r requirements.txt```.
2. Create ```.env``` file using ```example.env``` and fill it with your data (copy secret key, setup db).
3. Set secret key, debug and db options in ```settings.py```.
```py
from decouple import config
...
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```
4. Change your path to project directory and run the server.
```sh
> python manage.py runserver
```
5. Apply migrations.
```sh
> python manage.py migrate
```