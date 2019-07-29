rmdir /s /q WebApp\migrations


del db.sqlite3
python manage.py makemigrations WebApp

python3 manage.py migrate
python3 manage.py createsuperuserwithpassword    --username nsdevil --password nsdevil --email admin@example.org    --preserve

python3 manage.py runserver