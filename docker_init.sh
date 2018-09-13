#!/usr/bin/env bash

docker-compose build
docker-compose up -d
docker-compose exec flaskapp python manage.py db migrate
docker-compose exec flaskapp python manage.py db upgrade


echo ''
echo '-------------------------------------'
echo ''
echo 'The cluster has been initialized'
echo 'Navigate to http://localhost:8080'
echo 'to see the running flask app'
echo ''
echo '-------------------------------------'
echo ''