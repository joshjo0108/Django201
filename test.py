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

    # ADDING LOG IN / LOG OUT / PASSWORD
        # pipenv install django-allauth

# MAKE profiles FOLDER
    # python3 manage.py startapp profiles   
    # python3 manage.py makemigrations
    # python3 manage.py migrate 

# WHEN MAKING javascript file
    #  python3 manage.py collectstatic


# CREATE A FOLDER followers
    #  python3 manage.py startapp followers
    # THEN ADD "followers" ON "INSTALLED_APPS = []" IN "settings.py"

# AFTER UPDATING ON "admin.py"
    # RUN "python3 manage.py makemigrations"
    # python3 manage.py migrate