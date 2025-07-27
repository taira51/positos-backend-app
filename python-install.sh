docker-compose run \
  --entrypoint "poetry init \
    --name positos-backend-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  ai-positos-backend-app