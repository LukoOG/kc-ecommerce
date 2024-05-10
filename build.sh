set -oerrexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations
pythom manage.py migrate