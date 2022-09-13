python 3.9
django 4.0~4.1
bootstrap -v 4

始め方
docker compose up -d

変更時
docekr compose restart

止め方と再開
docker compose stop
docker comopse start
終了時
docker compose down -v



makemigrations:
  docker compose run --rm web python manage.py makemigrations fec_app_folder

migrate:
  docker compose run --rm web python manage.py migrate
createsuperuser:
  docker compose run --rm web python manage.py createsuperuser


