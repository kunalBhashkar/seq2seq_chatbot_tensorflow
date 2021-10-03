#!/bin/bash

docker build -t \
    chat-bot:packaged \
    -f Dockerfile.packaged \
    .

docker tag chat-bot:packaged robsokolowski/chat-bot:packaged
docker push robsokolowski/chat-bot:packaged
