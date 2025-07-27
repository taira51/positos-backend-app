# positos-backend-app

### 関連URL
1. [Swagger UI（ローカル）](http://localhost:8000/docs)


### 環境構築コマンド
| 概要                               | コマンド                                                                 |
|------------------------------------|--------------------------------------------------------------------------|
| Docker image作成                  | `docker-compose build`|
| Docker起動                        | `docker-compose up`|
| DBマイグレーション（テーブル作成・初期化） | `docker-compose exec api poetry run python -m api.migrate_db`|
| MySQL接続                         | `docker-compose exec db mysql positos`|
| Dockerコンテナ状態一覧           | `docker-compose ps`|
| Dockerコンテナに接続             | `docker exec -it [CONTAINER_ID] /bin/sh`|
