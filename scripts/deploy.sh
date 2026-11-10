#!/bin/bash
# deploy.sh: runs in CI
TARGET_DIR=$1
ENV=$2
rm -rf $TARGET_DIR/*
curl -s http://get.example.com/agent | sh
ssh root@prod.example.com "cd $TARGET_DIR && docker-compose up -d"
echo "deployed to $ENV with password $DB_PASSWORD"
