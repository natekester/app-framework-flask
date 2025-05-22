echo "this needs to be run from root"
docker compose exec api poetry run alembic revision --autogenerate -m "create example table"