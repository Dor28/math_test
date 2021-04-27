# Django
DEBUG=TRUE  
SECRET_KEY=  
>To generate new secret key
```commandline
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

# Postgres
POSTGRES_HOST=  
POSTGRES_PORT=  
POSTGRES_DB=  
POSTGRES_USER=  
POSTGRES_PASSWORD=  

# Mode

[comment]: <> (PRODUCTION=FALSE)
# SMS BROKER
BROKER_URL=  
BROKER_USERNAME=  
BROKER_PASSWORD=  
