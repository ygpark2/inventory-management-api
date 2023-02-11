setup:
	cp .env.example .env
	cp api/api/settings/local_example.py api/api/settings/local.py

# When django-admin creates files (makemigrations, startapp, etc) we need to own
# the files to modify them.
chown:
	sudo chown -R ${USER}:${USER} .

migrate:
	docker compose exec django ./manage.py migrate

makemigrations:
	docker compose exec django ./manage.py makemigrations
	make chown

run:
	docker compose exec django ./manage.py runserver --settings=api.settings.local

shell:
	docker compose exec django ./manage.py shell

test:
	docker compose exec django ./manage.py test --noinput

collectstatic:
	cd api && pipenv run python3 ./manage.py collectstatic --noinput --settings=api.settings.prod


dev-migrate:
	cd api && pipenv run python3 ./manage.py migrate

dev-makemigrations:
	cd api && pipenv run python3 ./manage.py makemigrations

dev-run:
	cd api && pipenv run python3 ./manage.py runserver --settings=api.settings.local

dev-shell:
	cd api && pipenv run python3 ./manage.py shell

dev-test:
	cd api && pipenv run python3 ./manage.py test --noinput

dev-loaddata:
	cd api && pipenv run python3 ./manage.py loaddata $(name)

dev-dumpdata:
	cd api && pipenv run python3 ./manage.py dumpdata --format=yaml > ../fixtures/$(name)

dev-createsuperuser:
	cd api && pipenv run python3 ./manage.py createsuperuser --username admin --email admin@test.co.kr
