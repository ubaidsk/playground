# Using multi-architecture builds for docker

```bash
colima start

docker buildx create --use --platform=linux/arm64,linux/amd64 --name multi-platform-builder

docker buildx build . --platform linux/amd64,linux/arm64 -t ubaids/flask-redis-service:0.1 --push
```