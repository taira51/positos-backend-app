docker-compose run \
  --entrypoint "poetry init \
    --name ai-todo-list-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  ai-todo-list-app