#######################
# Cmd projet Django   #
#######################

# Local development management
clean:
	find -L . -name "*~" -exec rm -fr {} \;
	find -L . -name "*.pyc" -exec rm -fr {} \;
	find -L . -name ".DS_Store" -exec rm -fr {} \;
	find -L . -name "Thumbs.db" -exec rm -fr {} \;
	find -L . -name "Thumbs.db:encryptable" -exec rm -fr {} \;

runserver:
	python manage.py runserver

cp_settings:
	-diff -u ./settings.py.example ./settings.py
	cp ./settings.py ./settings.py.example

dumpdata:
	python manage.py dumpdata --natural --exclude=admin --exclude=contenttypes --exclude=auth --exclude=sessions --format yaml --indent=4 > fimu_data.yaml

loaddata:
	python manage.py loaddata fimu_data.yaml

mail:
	python -m smtpd -n -c DebuggingServer localhost:1025

syncdb:
	python manage.py flushwebsite
	python manage.py syncdb --noinput --migrate
	python manage.py createsuperuser
	python manage.py loaddata fimu_data.yaml

# Testing suite
test:
	python -Wd manage.py test administration authentication page_blog

# Deployment management
collectstatic:
	python manage.py collectstatic --noinput

requirements:
	pip freeze > requirements.txt

upgrade:
	pip install -r requirements.txt

