docker-compose run \
  --entrypoint "poetry init \
    --name ai-todo-list-backend-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  ai-ai-todo-list-backend-app