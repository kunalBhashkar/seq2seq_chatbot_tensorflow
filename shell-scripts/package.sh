#!/bin/bash

docker build -t \
    chat-bot:packaged \
    -f Dockerfile.packaged \
    .
