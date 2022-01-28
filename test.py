# HOW TO SET UP DJANGO IN pipenv
    # pipenv install django
    # pipenv shell  -> starting the pipenv
    # django-admin startproject til .
    # python3 manage.py migrate -> WILL CREATE db.sqlite3 FILE
    # python3 manage.py runserver 0.0.0.0:8000
    # python3 manage.py createsuperuser     -> MAKING ID AND PASSWORD
    # python3 manage.py startapp feed -> NOT START PROJECT, CREATING A PROJECT NAMED 'feed'
    # python3 manage.py makemigrations -> making "feed/migrations" files WHEN YOU USE models.py
    # python3 manage.py migrate -> execute the above file
