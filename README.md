Python（django）

#### 本番環境
psql (PostgreSQL)
#### 開発環境
sqlite

nginx version: nginx/1.18.0 (Ubuntu)



## 共同開発者は以下を見てください
#### 始め方を実行してからmakemigrations以下を順に一回実行してください
#### そのあとは止め方と再開のみしか利用しない想定です。
### cssは可能か限りこれで書く
bootstrap4

### 始め方
docker compose up -d

### 変更時
docekr compose restart

### 止め方と再開
docker compose stop
docker comopse start
### 終了時
docker compose down -v


### makemigrations
  docker compose run --rm web python manage.py makemigrations fec_app_folder

### migrate
  docker compose run --rm web python manage.py migrate
### createsuperuser
  docker compose run --rm web python manage.py createsuperuser


