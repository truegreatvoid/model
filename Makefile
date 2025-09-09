sync:
	uv sync

run:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
	uv run python manage.py runserver
# 	uv run uvicorn conf.asgi:application --host 0.0.0.0 --port 8005 --reload

app:
	uv run python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))
	mv $(filter-out $@,$(MAKECMDGOALS)) src/apps/$(filter-out $@,$(MAKECMDGOALS))

app_ext:
	uv run python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))
	mv $(filter-out $@,$(MAKECMDGOALS)) packages/model-apps/src/model_apps/$(filter-out $@,$(MAKECMDGOALS))

ruff:
	uvx ruff format .
