rm -r WebApp/migrations


fuser -k -n tcp 9010
rm db.sqlite3
python manage.py makemigrations WebApp

python manage.py migrate
python manage.py createsuperuserwithpassword    --username nsdevil --password nsdevil --email admin@example.org    --preserve
python manage.py runserver 0.0.0.0:9010