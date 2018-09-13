#!/usr/bin/env bash

# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi $(docker images -q)

echo ''
echo '-------------------------------------'
echo ''
echo 'All images and containers'
echo 'have been deleted! I hope you did'
echo 'not delete anything you need!'
echo ''
echo '-------------------------------------'
echo ''