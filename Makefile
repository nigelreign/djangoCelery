checkfiles = api/ config/ portal/ services/ users/

run:
	python3 manage.py runserver

deps:
	@pip install --upgrade pip
	@pip install -q pip-tools
	@pip-sync requirements.txt
	@pip install --no-cache-dir -qe  .


celery:
	celery -A djangoCelery worker -l info

# celery-beat:
# 	celery -A config beat -l info 

ci: deps style

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate


superuser:
	python3 manage.py createsuperuser

style:
	black $(checkfiles)
