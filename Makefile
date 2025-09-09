sync:
	uv sync

run:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
	uv run python manage.py runserver 0.0.0.0:8000
# 	uv run uvicorn conf.asgi:application --host 0.0.0.0 --port 8005 --reload