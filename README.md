 # Django Rest Framework backend for https://github.com/paramore21/diploma 
 1.Создать .env файл и сгенерировать SECRET_KEY =    
 `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key()`   
 Работает на линукс, на windows смотрите документацию.
 
 2. Установить необходимые библиотеки.   
  `pip install -r requirements.txt`
 3. `python manage.py makemigrations`   
 4. `python manage.py migrate`   
 5. `python manage.py runserver`
